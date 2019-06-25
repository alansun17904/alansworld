from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'archives/index.html')

def psychology(request):
    return render(request,'archives/psychology/psychology.html')

def workinprogress(request):
    return render(request, 'archives/workinprogress.html')