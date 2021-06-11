from django.shortcuts import redirect, render, get_object_or_404
from .models import Event
from .forms import CommentForm, EventForm

def home(request):
    events = Event.objects.all()
    data = {
        'title': 'Event Home page',
        'data': events
    }
    return render(request, 'table.html', context=data)


def event_detail(request, event_id):
    single_event = get_object_or_404(Event, id=event_id)
    form_event = EventForm(instance=single_event)
    if request.POST:
        form = CommentForm(request.POST)
        form_event = EventForm(request.POST, instance=single_event)
        if form.is_valid():
            form.instance.user = request.user
            form.instance.event = single_event
            form.save()
            return redirect('home-page')
        if form_event.is_valid():
            form_event.save()
            return redirect('home-page')

    form = CommentForm()
    
    data = {
        'data': single_event,
        'form': form,
        'e_form': form_event
    }
    return render(request, 'event-detail.html', context=data)


def sme_details(request, sme_id):
    form_event = EventForm(instance=single_sme)
    if request.POST:
        form = CommentForm(request.POST)
        form_event = EventForm(request.POST, instance=single_sme)
        if form.is_valid():

            form.instance.user = request.user
            form.instance.event = single_sme
            form.save()
            return redirect('home-page')
        if form_event.is_valid():
            form_event.save()
            return redirect('home-page')

    form = CommentForm()
    
    data = {
        'data': single_sme,
        'form': form,
        'e_form': form_event
    }
    return render(request, 'sme-detail.html', context=data)


def form_demo(request):
    form  = EventForm()
    data = {
        'form': form
    }
    return render(request, 'form-demo.html', context=data)