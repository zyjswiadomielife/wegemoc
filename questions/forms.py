from django.forms import ModelForm
from .models import Question, Answer

class QuestionAdd(ModelForm):
    
    class Meta:
        model = Question
        fields = ['title', 'body', 'tags']

class AnswerAdd(ModelForm):

    class Meta:
        model = Answer
        fields = ['body']