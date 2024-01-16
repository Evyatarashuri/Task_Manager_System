from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse

def login_user(request):
    return render(request, "html/login.html")

def ashuri (request):
    return HttpResponse("ashuri!")