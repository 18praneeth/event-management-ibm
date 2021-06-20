from django.shortcuts import redirect, render, get_object_or_404
from .models import Event, CollegeName, SMEProfile
from django.contrib.auth.models import User
from .forms import CollegeForm, CommentForm, EventUpdateForm, EventCreateForm, EventAssignForm, SMEForm
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.contrib import messages
from .utils import send_slack_message


@login_required
def home(request):
    if request.user.is_superuser:
        events = Event.objects.all()
        assigned_event = Event.objects.filter(assigned_user=request.user)
    else:
        events = Event.objects.filter(publish=True, status="Planned")
        assigned_event = Event.objects.filter(assigned_user=request.user)
    data = {
        'title': 'Event Home page',
        'data': events,
        'data2': assigned_event
    }
    return render(request, 'table.html', context=data)


@login_required
def college_details(request):
    college=CollegeName.objects.all()
    context={
        'title':'College Details',
        'data':college
    }
    return render(request,'college-table.html',context=context)


@login_required
def create_college(request):
    c_form = CollegeForm()

    if request.POST:
        c_form = CollegeForm(request.POST)
        if c_form.is_valid():
            c_form.save()
            messages.success(request,'The college is created')
            return redirect('college-details')
    return render(request, 'create.html', context={'form':c_form, 'button_text': 'Create college'})


@login_required
def college_edit(request, id):
    college = get_object_or_404(CollegeName, id=id)
    form = CollegeForm(instance=college)
    if request.POST:
        form = CollegeForm(request.POST, instance=college)
        if form.is_valid:
            form.save()
            return redirect('college-details')
    
    context = {
        'title': "Edit College detail",
        'form': form,
        'button_text': 'Update College'
    }

    return render(request, 'event-edit.html', context)

@login_required
def college_delete(request,id):
    college=get_object_or_404(CollegeName,id=id)
    college.delete()
    return redirect('college-details')


@login_required
def event_detail(request, event_id):
    single_event = get_object_or_404(Event, id=event_id)
    a_form = EventAssignForm(instance=single_event)
    c_form = CommentForm()
    if request.POST:
        val = request.POST.get('hidden_option')

        if val == "1":
            single_event.publish = True
            single_event.save()
            send_slack_message(single_event)
            return redirect('event-detail', event_id=event_id)
        elif val == "0":
            single_event.publish = False
            single_event.save()
            return redirect('event-detail', event_id=event_id)

        c_form = CommentForm(request.POST)
        a_form = EventAssignForm(request.POST, instance=single_event)

        if c_form.is_valid():
            c_form.instance.user = request.user
            c_form.instance.event = single_event
            messages.success(request, 'Your comment is posted')
            c_form.save()
            return redirect('event-detail', event_id=event_id)

        if a_form.is_valid():
            event = a_form.save()
            event.status = 'Assigned'
            event.save()
            return redirect('event-detail', event_id=event_id)

    data = {
        'data': single_event,
        'form': c_form,
        'a_form': a_form
    }
    return render(request, 'event-detail.html', context=data)


@login_required
def event_delete(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    event.delete()
    messages.error(request,'The event is deleted')
    return redirect('event')


@login_required
def event_update(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    e_form = EventUpdateForm(instance=event)

    if request.POST:
        e_form = EventUpdateForm(request.POST, instance=event)
        if e_form.is_valid():
            e_form.save()
            messages.success(request,'The event is updated')
            return redirect('event-detail', event_id=event_id)
    
    context = {
        'form': e_form,
        'button_text': 'Update Event'
    }
    return render(request, 'event-edit.html', context)


@login_required
def create_event(request):
    form = EventCreateForm()
    if request.POST:
        form = EventCreateForm(request.POST)
        if form.is_valid():
            event = form.save()
            messages.success(request, 'Your event is Created')
            return redirect('event')
    
    context = {
        'form': form,
    }
    return render(request, 'create-event.html', context=context)


@login_required
def signup_event(request, id):
    event = get_object_or_404(Event, id=id)
    event.accepted_users.add(request.user)
    messages.success(request, 'You have successfully signed up for the event.')
    return redirect('event')


@login_required
def mail_signup(request, id):
    event = get_object_or_404(Event, id=id)
    messages.success(request,'You have signed up to your email')
    context = {
        'event': event
    }
    return render(request, 'mail-signup.html', context)




# @login_required
# def create_sme(request):
#     form = SMEProfile()
#     if request.POST:
#         form = SMEProfile(request.POST)
#         if form.is_valid():
#             form.save()
#         return redirect('sme-list')
    
#     context = {
#         'form': form,
#         'button_text': 'Create SME'
#     }
#     return render(request, 'create.html', context)


@login_required
def edit_sme(request, id):
    sme = get_object_or_404(SMEProfile, id=id)
    form = SMEForm(instance=sme)
    if request.POST:
        form = SMEForm(request.POST, instance=sme)
        if form.is_valid():
            form.save()
        return redirect('sme-list')
    
    context = {
        'form': form,
        'button_text': 'Save SME'
    }
    return render(request, 'create.html', context)
