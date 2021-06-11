from django.shortcuts import redirect, render
from django.contrib.auth import logout

def home(request):
    data = {
        'title': 'User Home page'
    }
    return render(request, 'base.html', context=data)


def user_logout(request):
    logout(request)
    return redirect('event')
