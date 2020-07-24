from django.urls import re_path
from django.contrib.auth.decorators import login_required
from questions.models import Question, Answer
     
from . import views
from .models import LikeDislike
from recipes.models import Embed
     
app_name = 'ajax'
urlpatterns = [
    re_path(r'^embed/(?P<pk>\d+)/like/$',
        login_required(views.VotesView.as_view(model=Embed)),
        name='embed_like'),
    re_path(r'^question/(?P<pk>\d+)/like/$',
        login_required(views.VotesView.as_view(model=Question)),
        name='question_like'),
    re_path(r'^answer/(?P<pk>\d+)/like/$',
        login_required(views.VotesView.as_view(model=Answer)),
        name='answer_like'),
]