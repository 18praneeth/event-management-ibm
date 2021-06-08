from django.shortcuts import render
from .models import Event

def home(request):
    event = Event.objects.all()
    data = {
        'title': 'Event Home page',
        'data': event
    }
    return render(request, 'base.html', context=data)
