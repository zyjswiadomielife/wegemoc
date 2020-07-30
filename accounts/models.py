from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from stream_django.feed_manager import feed_manager
from stream_django.activity import Activity
from django.dispatch import receiver
import gdpr_assist

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=gdpr_assist.ANONYMISE(models.SET_NULL))
    avatar = models.ImageField(upload_to='avatar', verbose_name='Awatar profilu', default='defaultavatar.png')
    bio = models.TextField(verbose_name='O mnie', blank=True)
    url = models.URLField(max_length=255, verbose_name='Link do bloga lub innej strony', blank=True, null=True)
    facebook = models.URLField(max_length=255, verbose_name='Profil lub fanpage na Facebooku', blank=True, null=True)

    def __str__(self):
        return 'Profil użytkownika {}'.format(self.user.username)

    class PrivacyMeta:
        fields = ['bio', 'url', 'facebook']

        def anonymise_private_data(self, instance):
            return 0


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class Follow(Activity, models.Model):
    user = models.ForeignKey(User, on_delete=gdpr_assist.ANONYMISE(models.SET_NULL), related_name='following')
    target = models.ForeignKey(User, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'target')

    @classmethod
    def activity_related_models(cls):
        return ['user', 'target']
    
    @property
    def activity_object_attr(self):
        return self
    
    @property
    def activity_notify(self):
        target_feed = feed_manager.get_notification_feed(self.target_id)
        return [target_feed]

    class PrivacyMeta:
        export_exclude = ['deleted_at']

        def anonymise_private_data(self, instance):
            return 0

def unfollow_feed(sender, instance, **kwargs):
    feed_manager.unfollow_user(instance.user_id, instance.target_id)


def follow_feed(sender, instance, created, **kwargs):
    if created:
        feed_manager.follow_user(instance.user_id, instance.target_id)


post_save.connect(follow_feed, sender=Follow)
post_delete.connect(unfollow_feed, sender=Follow)

class UserPrivacyMeta:
    fields = ['first_name', 'last_name', 'email', 'username']
    search_fields = ['username']

gdpr_assist.register(User, UserPrivacyMeta)