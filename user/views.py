from django.shortcuts import render

def home(request):
    data = {
        'title': 'User Home page'
    }
    return render(request, 'base.html', context=data)