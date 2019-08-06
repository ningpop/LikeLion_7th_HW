from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from .models import Teacher

# Create your views here.

def home(request):
    return render(request, 'home.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def beateacher(request):
    return render(request, 'beateacher.html')

def findmyteacher(request):
    teacher = Teacher.objects
    return render(request, 'findmyteacher.html', {'teacher':teacher})