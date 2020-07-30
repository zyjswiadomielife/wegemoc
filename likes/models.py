from django.db import models
from django.db.models import Sum
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.auth.models import User
from stream_django.activity import Activity
import gdpr_assist

     
class Like(models.Model, Activity):

    user = models.ForeignKey(User, verbose_name='uzytkownicy', on_delete=gdpr_assist.ANONYMISE(models.SET_NULL))
    created_at = models.DateTimeField(auto_now_add=True)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()

    @property
    def activity_actor_attr(self):
        return self.user

    class PrivacyMeta:
        fields = ['user']

        def anonymise_private_data(self, instance):
            return 0

        