from user.forms import RangeRequestForm, UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import logout
from django.contrib import messages
from djqscsv import render_to_csv_response
from event.models import Event


def user_logout(request):
    messages.info(request, 'You have logged out!!')
    logout(request)
    return redirect('event')


def csv_export(request):
    form = RangeRequestForm()
    if request.POST:
        form = RangeRequestForm(request.POST)
        if form.is_valid():
            start = form.cleaned_data['start']
            end = form.cleaned_data['end']

            qs = Event.objects.filter(date__gte=start, date__lte=end).values('id','event_activity_type','technology_tracks','event_activity_mode','organised_by','session_topic_name','session_duration','number_of_attendees','institution_name__college_name', 'institution_name__college_city','institution_name__college_state','institution_name__college_region','sme__sme_name','sme__sme_notes_id','sme__sme_manager_notes_id','sme__sme_bu','ur_spoc','link','status','college_category')
            response = render_to_csv_response(qs,
            filename='Report',
            field_header_map={
                    'id':'ID',
                    'event_activity_type':'Event Activity Type',
                    'technology_tracks':'Technology Tracks',
                    'event_activity_mode':'Event Activity Mode',
                    'organised_by':'Organised By',
                    'session_topic_name':'Session Topic Name',
                    'session_duration':'Session Duration',
                    'number_of_attendees':'Number Of Attendees',
                    'institution_name__college_name':'College Name',
                    'institution_name__college_city':'College City',
                    'institution_name__college_state':'College State',
                    'institution_name__college_region':'College Region',
                    'sme__sme_name':'SME Name',
                    'sme__sme_notes_id':'SME Notes ID',
                    'sme__sme_manager_notes_id':'SME Manager Notes ID',
                    'sme__sme_bu':'SME BU',
                    'ur_spoc':'UR SPOC',
                    'link':'Link',
                    'status':'Status',
                    'college_category':'College Category',
                }
            )
            return response
    
    context = {
        'form': form
    }
    return render(request, 'report.html', context)


@login_required
def profile(request):
    user = get_object_or_404(User, id=request.user.id)
    context = {
        'user': user
    }
    return render(request, 'profile.html', context)


@login_required
def register(request):
    if request.POST:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('edit-sme', id=user.smeprofile.id)
    else:
        form = UserRegisterForm()

    context = {
        'form': form,
        'button_text': 'Create SME'
    }
    return render(request, 'create.html', context)