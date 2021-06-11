from django.shortcuts import redirect, render, get_object_or_404
from .models import Event, SME
from .forms import CommentForm, EventForm, SMEForm

def home(request):
    events = Event.objects.all()
    data = {
        'title': 'Event Home page',
        'data': events
    }
    return render(request, 'table.html', context=data)


def event_detail(request, event_id):
    single_event = get_object_or_404(Event, id=event_id)
    e_form = EventForm(instance=single_event)
    if request.POST:
        c_form = CommentForm(request.POST)
        e_form = EventForm(request.POST, instance=single_event)
        if c_form.is_valid():
            c_form.instance.user = request.user
            c_form.instance.event = single_event
            c_form.save()
            return redirect('home-page')
        if e_form.is_valid():
            e_form.save()
            return redirect('home-page')

    c_form = CommentForm()
    
    data = {
        'data': single_event,
        'form': c_form,
        'e_form': e_form
    }
    return render(request, 'event-detail.html', context=data)


def create_sme(request):
    s_form = SMEForm()
    
    if request.POST:
        s_form = SMEForm(request.POST)
        if s_form.is_valid():
            s_form.save()
            print('New SME is created')
            return redirect('sme')

    return render(request, 'sme-detail.html', context={'s_form': s_form})

