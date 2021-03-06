from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import Follow
from stream_django.enrich import Enrich
from stream_django.feed_manager import feed_manager
from .forms import EditUser, EditProfile

def profile(request, username):
    profile = get_object_or_404(User, username=username)
    addedbyuser = profile.addedbyuser.all()
    return render(request, 'profile/detail.html', {'profile': profile,
                                                    'addedbyuser': addedbyuser})

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


@login_required
def editprofile(request):
    if request.method=='POST':
        user_form = EditUser(instance=request.user, data=request.POST)
        profile_form = EditProfile(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        user_form = EditUser(instance=request.user)
        profile_form = EditProfile(instance=request.user.profile)
    return render(request, 'profile/edit.html', {'user_form': user_form,
                                                 'profile_form': profile_form})