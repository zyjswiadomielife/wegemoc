from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.views.generic import ListView
from recipes.models import Embed
from .models import Bookmark
import json

@login_required
def bookmark(request, id):

    bookmark = get_object_or_404(Embed, id=id)

    bookmarks, created = Bookmark.objects.get_or_create(user=request.user,obj=bookmark)

    if not created:
        bookmarks.delete()

    return HttpResponse(
            json.dumps({
                "result": created,
                "count": Bookmark.objects.filter(obj_id=id).count()
            }),
            content_type="application/json"
        )

class UserBookmarksListView(LoginRequiredMixin, ListView):

    model = Bookmark
    paginate_by = 15
    template_name = 'bookmarks/user_bookmarks_list.html'
    context_object_name = 'bookmarks'

    def get_queryset(self, **kwargs):
        user = get_object_or_404(User, username=self.request.user)
        return user.userbookmarks.all()