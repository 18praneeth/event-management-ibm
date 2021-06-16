from django.shortcuts import redirect, render, get_object_or_404
from .models import Event
from .forms import CollegeForm, CommentForm, EventUpdateForm, EventCreateForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages


@login_required
def home(request):
    send_mail(
            'Subject here',
            'Here is the message.',
            'from@example.com',
            ['to@example.com'],
            fail_silently=False,
        )
    if request.user.is_superuser:
        events = Event.objects.all()
    else:
        events = Event.objects.filter(publish=True)
    data = {
        'title': 'Event Home page',
        'data': events
    }
    return render(request, 'table.html', context=data)


@login_required
def event_detail(request, event_id):
    single_event = get_object_or_404(Event, id=event_id)
    if request.POST:
        val = request.POST.get('hidden_option')
        if val == "1":
            single_event.publish = True
            single_event.save()
        elif val == "0":
            single_event.publish = False
            single_event.save()
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


@login_required
def event_delete(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    return redirect('event')


@login_required
def event_update(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    e_form = EventUpdateForm(instance=event)

    if request.POST:
        e_form = EventUpdateForm(request.POST, instance=event)
        if e_form.is_valid():
            e_form.save()
            return redirect('event-detail', event_id=event_id)
    
    context = {
        'e_form': e_form,
    }
    return render(request, 'event-edit.html', context)


@login_required
def create_event(request):
    form = EventCreateForm()
    
    context = {
        'form': form,
    }
    return render(request, 'create-event.html', context=context)

'''def create_event2(request):
    n_form=Eventform()

    context={
        'n_form': Eventform,
            }
    return render(request,'create-event.html',context=context)'''

def create_college(request):
    c_form = CollegeForm()

    if request.POST:
        c_form = CollegeForm(request.POST)
        if c_form.is_valid():
            c_form.save()
            return redirect('college')
    return render(request,'college-details.html',context={'c_form':c_form})



@login_required
def signup_event(request, id):
    event = get_object_or_404(Event, id=id)
    event.accepted_users.add(request.user)
    messages.success(request, 'You have successfully signed up for the event.')
    return redirect('event')



@login_required
def reject_event(request, id):
    event = get_object_or_404(Event, id=id)
    event.rejected_users.add(request.user)
    messages.error(request, 'You have Rejected the Event')
    return redirect('event')  


@login_required
def mail_signup(request, id):
    event = get_object_or_404(Event, id=id)
    context = {
        'event': event
    }
    return render(request, 'mail-signup.html', context)