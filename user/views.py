from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import logout
from django.contrib import messages

def home(request):
    data = {
        'title': 'User Home page'
    }
    return render(request, 'base.html', context=data)


def user_logout(request):
    messages.info(request, 'You have logged out!!')
    logout(request)
    return redirect('event')
