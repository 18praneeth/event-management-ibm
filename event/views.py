from django.shortcuts import redirect, render, get_object_or_404
from .models import Event
from .forms import CollegeForm, CommentForm, GeneralEventForm, SMEEventForm

def home(request):
    events = Event.objects.all()
    data = {
        'title': 'Event Home page',
        'data': events
    }
    return render(request, 'table.html', context=data)


def event_detail(request, event_id):
    single_event = get_object_or_404(Event, id=event_id)
    if request.POST:
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            c_form.instance.user = request.user
            c_form.instance.event = single_event
            c_form.save()
            return redirect('event')


    c_form = CommentForm()
    
    data = {
        'data': single_event,
        'form': c_form,
    }
    return render(request, 'event-detail.html', context=data)


def create_event(request):
    sme_form = SMEEventForm()
    g_form = GeneralEventForm()

    context = {
        's_form': sme_form,
        'g_form': g_form
    }
    return render(request, 'create-event.html', context=context)


def create_college(request):
    c_form = CollegeForm()

    if request.POST:
        c_form = CollegeForm(request.POST)
        if c_form.is_valid():
            c_form.save()
            return redirect('college')
    return render(request,'college-details.html',context={'c_form':c_form})