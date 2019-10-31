from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import Profile

# Create your views here.

def signup(request):
    if request.method == 'POST':
        user = User.objects.create_user(request.POST['id'], password=request.POST['password1'], email=request.POST['email'])
        user.profile.phone = request.POST['phoneNumber']
        user.profile.gender = request.POST['gender']
        auth.login(request, user)
        return redirect('home')
    return render(request, 'signup.html')


# def signup(request):
#     if request.method == "POST":
#         if request.POST['password1'] == request.POST['password2']:
#             try:
#                 user = User.objects.get(id=request.POST['id'])
#                 return render(request, 'signup.html', {'error': 'UserID has already been taken'})
#             except User.DoesNotExist:
#                 user = User.objects.create_user(
#                     request.POST['id'], password=request.POST['password1'])
#                 auth.login(request, user)
#                 return redirect('home')
#         else:
#             return render(request, 'signup.html', {'error': 'Passwords must match'})
#     else:
#         # User wants to enter info
#         return render(request, 'signup.html')

def login(request):
    if request.method == 'POST':
        id = request.POST['id']
        password = request.POST['password']
        user = auth.authenticate(request, id=id, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'UserID or password is incorrect.'})
    else:
        return render(request, 'login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'signup.html')