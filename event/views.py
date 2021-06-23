from django.shortcuts import redirect, render, get_object_or_404
from .models import Event, CollegeName, SMEProfile
from .forms import CollegeForm, CommentForm, EventUpdateForm, EventCreateForm, EventAssignForm, SMEForm
from django.contrib.auth.decorators import login_required
from dateutil import parser
from django.contrib import messages
from .utils import send_slack_message, send_mail_assigned


@login_required
def home(request):
    if request.user.is_superuser:
        events = Event.objects.all().order_by('-id')
        assigned_event = Event.objects.filter(assigned_user=request.user).order_by('-id')
    else:
        events = Event.objects.filter(publish=True, status="Planned").order_by('-id')
        assigned_event = Event.objects.filter(assigned_user=request.user).order_by('-id')
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

            assigned_list = []
            for user in event.assigned_user.all():
                assigned_list.append(user.email)
            send_mail_assigned(assigned_list, event)

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



@login_required
def sme_list(request):
    smes = SMEProfile.objects.all()
    context = {
        'smes': smes
    }
    return render(request, 'sme-list.html', context)


@login_required
def csv_upload(request):
    if request.POST:
        csv_file = request.FILES['csv_file']
        if len(csv_file) == 0:
            context = {
                'message': 'Please select only CSV files'
            }
            return render(request, 'csv_upload.html', context)
        
        file_data = csv_file.read().decode('utf-8')
        lines = file_data.split('\n')
        for index, line in enumerate(lines):
            fields = line.split(",")
            if index < 9:
                continue
            else:
                try:
                    date = parser.parse(f'{fields[2]} {fields[1]} {fields[3]}')
                    print('*' * 200)
                    event = Event(
                        date = date.date(),
                        event_activity_type = fields[5],
                        technology_tracks = fields[6],
                        event_activity_mode = fields[7],
                        organised_by = fields[8],
                        session_topic_name = fields[9],
                        session_duration = fields[10]
                    )
                    event.save()
                except IndexError:
                    continue

                

    return render(request, 'csv_upload.html')


# @login_required
# def upload_csv(request):
#     if 'GET' == request.method:
#         # csv_list = CsvUpload.objects.all()
#         # paginator = Paginator(csv_list, 7)
#         # page = request.GET.get('page')
#         # try:
#         #     csvdata = paginator.page(page)
#         # except PageNotAnInteger:
#         #     csvdata = paginator.page(1)
#         # except EmptyPage:
#         #     csvdata = paginator.page(paginator.num_pages)
#         # return render(request, 'upload_csv.html', {'csvdata': csvdata})
#         csvdata = CsvUpload.objects.all()
#         context = {'csvdata': csvdata}
#         return render(request, 'upload_csv.html', context)
#     try:
#         csv_file = request.FILES["csv_file"]

#         if len(csv_file) == 0:
#             messages.error(request, 'Empty File')
#             return render(request, 'upload_csv.html')

#         if not csv_file.name.endswith('.csv'):
#             messages.error(request, 'File is not CSV type')
#             return render(request, 'upload_csv.html')

#         if csv_file.multiple_chunks():
#             messages.error(request, 'Uploaded file is too big (%.2f MB).' % (csv_file.size / (1000 * 1000),))
#             return render(request, 'upload_csv.html')

#         file_data = csv_file.read().decode("utf-8")

#         lines = file_data.split("\n")
#         for index, line in enumerate(lines):
#             fields = line.split(",")
#             if index == 0:
#                 if (fields[0] == 'name') and (fields[1] == 'description') and (fields[2] == 'end_date') and (
#                         fields[3] == 'notes'):
#                     pass
#                 else:
#                     messages.error(request, 'File is not Correct Headers')
#                     return render(request, 'upload_csv.html')
#                     break
#             else:
#                 print(index)
#                 if (len(fields[0]) != 0) and (len(fields[1]) != 0) and (len(fields[2]) != 0) and (len(fields[3]) != 0):
#                     data = CsvUpload(
#                         name=fields[0],
#                         description=fields[1],
#                         end_date=datetime.datetime.now(),
#                         notes=fields[3]
#                     )
#                     data.save()
#         messages.success(request, "Successfully Uploaded CSV File")
#         return redirect('/upload/csv/')

#     except Exception as e:
#         messages.error(request, "Unable to upload file. " + e)
#         return redirect('/upload/csv/')