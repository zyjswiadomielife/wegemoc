from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Follow
from stream_django.enrich import Enrich
from stream_django.feed_manager import feed_manager

def profile(request, username):
    enricher = Enrich()
    profile = get_object_or_404(User, username=username)
    feed = feed_manager.get_user_feed(profile.id)
    activities = feed.get(limit=25)['results']
    activities = enricher.enrich_activities(activities)
    return render(request, 'profile/detail.html', {'profile': profile,
                                                    'activities': activities})

@login_required
def follow(request, id):

    user = get_object_or_404(User, id=id)

    follow, created = Follow.objects.get_or_create(user=request.user,target=user)

    return HttpResponse()

@login_required
def unfollow(request, id):

    user = get_object_or_404(User, id=id)

    follow, created = Follow.objects.get_or_create(user=request.user,target=user)
    follow.delete()

    return HttpResponse()