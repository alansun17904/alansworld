from django.shortcuts import render
# from .models import PsychologyStudy, PsychologyQuestion
from archives.model import PsychologyStudy, PsychologyQuestion


def index(request):
    return render(request, 'archives/index.html')

def psychology(request):

    return render(request,'archives/psychology/psychology.html')

def workinprogress(request):
    return render(request, 'archives/workinprogress.html')