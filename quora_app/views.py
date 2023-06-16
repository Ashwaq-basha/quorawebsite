from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Question, Answer, Like
from .forms import QuestionForm, AnswerForm


def index(request):
    questions = Question.objects.all().order_by('-created_at')
    return render(request, 'index.html', {'questions': questions})


@login_required
def create_question(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.created_by = request.user
            question.save()
            return redirect('index.html')
    else:
        form = QuestionForm()
    return render(request, 'create_question.html', {'form': form})

@login_required
def answer_question(request, question_id):
    question = Question.objects.get(pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.created_by = request.user
            answer.question = question
            answer.save()
            return redirect('index.html')
    else:
        form = AnswerForm()
    return render(request, 'answer_question.html', {'question': question, 'form': form})

@login_required
def like_answer(request, answer_id):
    answer = Answer.objects.get(pk=answer_id)
    like, created = Like.objects.get_or_create(user=request.user, answer=answer)
    if not created:
        like.delete()
    return redirect('index.html')
