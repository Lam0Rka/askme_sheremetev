from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
from app.models import Question, Answer, Tag
import string
from django.db import models
from django.db.models import Count
# Create your views here.

QUESTIONS = [
    {
        "id": i,
        "title": f"Questions {i}",
        "text": f"This is question number {i}",
        "tag": f"Tag {i}",
        "answers": f"Answers {i}"
    } for i in range(200) # Eto kakoi-to list comprehation 10 shtuk takih delaetsia
]

ANSWER_QUESTIONS = [
    {
        "text": f"Test text, text text {i}"
    } for i in range(10)
]

QUESTIONS_QUESTION = [
    {
        "title": "Questions 1",
        "text": "This is question number 1",
        "tag": "tag_1"
    }
]

TAGS = [
    {
        "tag": f"Tag_{i+1}"
    } for i in range(5)
]

BEST_MEMBERS = [
    {
        "member": f"Best_{i+1}"
    } for i in range(5)
]

USER = [
    {

    }
]



def index(request):
    paginate_obj = paginate(Question.objects.get_new(), request)
    return render(request, 'index.html', {"questions": paginate_obj, "tags": TAGS, "members": BEST_MEMBERS})


def hot(request):
    paginate_obj = paginate(Question.objects.get_hot(), request)
    return render(request, template_name='hot.html', context= {"questions": paginate_obj, "tags": TAGS, "members": BEST_MEMBERS})

def ask(request):

    return render(request, 'ask.html', context= {"questions": QUESTIONS, "tags": TAGS, "members": BEST_MEMBERS})


def login(request):

    return render(request, 'login.html', context= {"questions": QUESTIONS, "tags": TAGS, "members": BEST_MEMBERS})


def question(request, question_id):
    
    item = Question.objects.get(pk=question_id)
    answers = Answer.objects.annotate(answer_likes_count=models.Count('answerlike')).filter(question_id=question_id)
    page_obj = paginate(answers, request)
    return render(request, 'question.html', {"answers": page_obj, "tags": TAGS, "members": BEST_MEMBERS, "question": item})



def tag(request, tag_name):
    page_obj = paginate(Question.objects.get_by_tag(tag_name), request)
    return render(request, "tag.html", {"tag_name": tag_name, "questions": page_obj, "tags": TAGS, "members": BEST_MEMBERS,})


def settings(request):

    return render(request, 'settings.html', {"questions": QUESTIONS, "tags": TAGS, "members": BEST_MEMBERS})

def signup(request):

    return render(request, 'signup.html', {"questions": QUESTIONS, "tags": TAGS, "members": BEST_MEMBERS})


def paginate(object_list, request, per_page=10):
    page_num = request.GET.get('page', 1)
    
    paginator = Paginator(object_list, 5)
    try:
        if not page_num.isdigit():
            page_num = 1
    except:
        pass

    if int(page_num) > paginator.num_pages:
        page_num = paginator.num_pages

    page_obj = paginator.page(page_num)
    return page_obj
