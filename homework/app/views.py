from django.shortcuts import render
from django.http import HttpResponse
from django.core.paginator import Paginator
import string

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
    paginate_obj = paginate(QUESTIONS, request)
    return render(request, 'index.html', {"questions": paginate_obj, "tags": TAGS, "members": BEST_MEMBERS})


def hot(request):
    paginate_obj = paginate(QUESTIONS[5:], request)
    return render(request, template_name='hot.html', context= {"questions": paginate_obj, "tags": TAGS, "members": BEST_MEMBERS})


def ask(request):

    return render(request, 'ask.html', context= {"questions": QUESTIONS, "tags": TAGS, "members": BEST_MEMBERS})


def login(request):

    return render(request, 'login.html', context= {"questions": QUESTIONS, "tags": TAGS, "members": BEST_MEMBERS})


def question(request, question_id):
    paginate_obj = paginate(ANSWER_QUESTIONS, request)
    return render(request, 'question.html', {"answers": paginate_obj, "tags": TAGS, "members": BEST_MEMBERS, "questions": QUESTIONS_QUESTION})


def tag(request, tag_name):
    paginate_obj = paginate(QUESTIONS, request)
    return render(request, 'tag.html', {"questions": paginate_obj, "tags": TAGS, "members": BEST_MEMBERS, "tag_name": tag_name})


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
