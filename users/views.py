from django.shortcuts import render
from users.forms import UserLoginForm, UserRegistrationForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse


# Create your views here.

def login(request):
    if request.method == 'POST':
        login_form = UserLoginForm(data=request.POST)
        if login_form.is_valid():
            data = {'username': request.POST.get('username'), 'password': request.POST.get('password')}
            login_user = auth.authenticate(**data)
            if login_user and login_user.is_active:
                auth.login(request, login_user)
                return HttpResponseRedirect(reverse('index'))
        else:
            print(login_form.errors)
    else:
        login_form = UserLoginForm()
    context = {'title': 'Login page', 'form': login_form}
    return render(request, 'users/login.html', context=context)


def registration(request):
    if request.method == 'POST':
        registration_form = UserRegistrationForm(data=request.POST)
        if registration_form.is_valid():
            registration_form.save()
            return HttpResponseRedirect(reverse('users:login'))
        else:
            print(registration_form.errors)
    else:
        registration_form = UserRegistrationForm()
    context = {'title': 'Registration page', 'form': registration_form}
    return render(request, 'users/registration.html', context=context)


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))
