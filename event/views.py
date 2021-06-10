from django.shortcuts import redirect, render, get_object_or_404
from .models import Event
from .forms import CommentForm

def home(request):
    events = Event.objects.all()
    data = {
        'title': 'Event Home page',
        'data': events
    }
    return render(request, 'table.html', context=data)


def event_detail(request, event_id):
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['comment'])
            return redirect('home')

    form = CommentForm()
    single_event = get_object_or_404(Event, id=event_id)
    data = {
        'data': single_event,
        'form': form
    }
    return render(request, 'event-detail.html', context=data)
