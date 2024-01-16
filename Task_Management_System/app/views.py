from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("hello world") # Httpresponse 

def evyatar(request):
    return render(request, "app/web.html") #render - html file 