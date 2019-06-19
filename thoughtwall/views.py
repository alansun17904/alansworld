from django.shortcuts import render
from .models import Question, Tag


def index(request):
    context = {
        "questions": Question.objects.all(),
        "tags": Tag.objects.all()
    }
    return render(request, "thoughtwall/index.html", context)
