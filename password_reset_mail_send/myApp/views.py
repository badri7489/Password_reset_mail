from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginForm, NewPasswordForm
from django.contrib.auth import login, authenticate
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.

def LoggedPage(request):
    return HttpResponse('You have successfully logged in.')

def LoginPage(request):
    form = LoginForm()
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('hogaya')
        else:
            messages.info(request, 'Username or Password Galat hai!!')
    context = {'form': form}
    return render(request, 'myApp/login.html', context)

def pass_reset(request):

    context = {}
    return render(request, 'myApp/pass_reset.html', context)

def pass_reset_mail_sent(request):
    return HttpResponse('Reset Password request was successful and mail has been sent if mail entered was correct!!')

def pass_new(request):
    context = {}
    return render(request, 'myApp/pass_new.html', context)
