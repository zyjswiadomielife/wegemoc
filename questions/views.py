from django.shortcuts import render, get_object_or_404, redirect
from .models import Question, Answer
from .forms import QuestionAdd, AnswerAdd
from django.contrib.auth.decorators import login_required

def questionlist(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'questions/list.html',
                {'questions': questions})


def questiondetail(request, slug):
    question = get_object_or_404(Question, slug=slug)
    answers = question.answers.all().order_by('-created_at')

    if request.method == 'POST':
        form = AnswerAdd(request.POST)
        if form.is_valid():
            new_answer = form.save(commit=False)
            new_answer.question = question
            new_answer.author = request.user
            new_answer.save()
    else:
        form = AnswerAdd()

    return render(request, 'questions/detail.html',
                    {'question': question,
                    'answers': answers,
                    'form': form})

@login_required
def questionadd(request):
    
    if request.method == 'POST':
        form = QuestionAdd(request.POST)
        if form.is_valid():
            new_question = form.save(commit=False)
            new_question.author = request.user
            new_question.save()
            form.save_m2m()
            return redirect('questiondetail', slug=new_question.slug)
    else:
        form = QuestionAdd()
    return render(request, 'questions/add.html',
                {'form': form})