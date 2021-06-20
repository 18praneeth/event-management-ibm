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
    qs = Event.objects.all().values('id','event_activity_type','technology_tracks','event_activity_mode','organised_by','session_topic_name','session_duration','number_of_attendees','institution_name__college_name', 'institution_name__college_city','institution_name__college_state','institution_name__college_region','sme_name','sme_notes_id','sme_manager_notes_id','sme_bu','ur_spoc','link','status','college_category')
    return render_to_csv_response(qs,
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
        'sme_name':'SME Name',
        'sme_notes_id':'SME Notes ID',
        'sme_manager_notes_id':'SME Manager Notes ID',
        'sme_bu':'SME BU',
        'ur_spoc':'UR SPOC',
        'link':'Link',
        'status':'Status',
        'college_category':'College Category',

    }
    )


@login_required
def profile(request):
    user = get_object_or_404(User, id=request.user.id)
    context = {
        'user': user
    }
    return render(request, 'profile.html', context)