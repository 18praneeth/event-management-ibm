from django.db import models
from django.contrib.auth.models import User
from .choice import *
import datetime



class CollegeName(models.Model):
    college_name = models.CharField(max_length=500,null=True, blank=True )
    college_city = models.CharField(max_length=500,null=True, blank=True,verbose_name='City')
    college_state=models.CharField(max_length=500, null=True, blank=True,verbose_name='State')
    college_region=models.CharField(max_length=500, choices=REGION_OPTION, null=True, blank=True,verbose_name='Region')


    def __str__(self):
        return self.college_name



class Smeprofile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ambassodor = models.CharField(max_length=500, choices=BOOLEAN_OPTION, blank=True)
    sme_name=models.CharField(max_length=100,null=True, blank=True,verbose_name='Name')
    sme_notes_id=models.CharField(max_length=100, verbose_name='Notes ID',null=True, blank=True)
    sme_manager_notes_id=models.CharField(max_length=100 , verbose_name=' Manager Notes ID',null=True, blank=True)
    sme_bu = models.CharField(max_length=500, choices=BU_OPTION, null=True, blank=True,verbose_name='BU')
    sme_location = models.CharField(max_length=500, null=True, blank=True, verbose_name='Location')


    def __str__(self):
        return f'{self.sme_name}'


class Event(models.Model):
    date = models.DateField(blank=True, null=True, default=datetime.date.today)
    event_activity_type = models.CharField(max_length=500, choices=EVENT_OPTION, null=True, blank=True,verbose_name='Activity Type')
    technology_tracks = models.CharField(max_length=500, choices=TRACKS_OPTION, null=True, blank=True, verbose_name='Technology Tracks')
    event_activity_mode = models.CharField(max_length=500, choices=EVENT_MODE_OPTION, null=True, blank=True,verbose_name='Activity Mode')
    organised_by = models.CharField(max_length=500, choices=ORGANISED_OPTION, null=True, blank=True)
    session_topic_name = models.CharField(max_length=100, blank=True, null=True)
    session_duration = models.CharField(max_length=500, choices=SESSION_OPTION, null=True, blank=True,verbose_name='Duration', help_text='Session Duration in hours.')
    number_of_attendees = models.IntegerField(default=0, null=True, blank=True)
    institution_name = models.ForeignKey(CollegeName, blank=True, null=True, on_delete=models.SET_NULL)
    ur_spoc = models.CharField(max_length=500, choices=URSPOC_OPTION, null=True, blank=True,verbose_name='UR SPOC')
    link = models.URLField(null=True, blank=True, help_text='Link of Academic Initiative Course/platform to be used from  https://ibm.biz/academic')
    status = models.CharField(max_length=500, choices=STATUS_OPTION, null=True, blank=True)
    signup_by = models.DateField(blank=True, null=True, default=datetime.date.today, verbose_name="Signup by")
    college_category = models.CharField(max_length=500, choices=COLLEGE_OPTION, null=True, blank=True)
    publish = models.BooleanField(default=False, help_text='Tick the option if you want to publish the event')
    accepted_users = models.ManyToManyField(User, help_text='Accepted Users', related_name='accepted_user', blank=True)
    assigned_user = models.ManyToManyField(User, blank=True, help_text='Event Assigneed')
    connected_event = models.ForeignKey(to='Event', null=True, blank=True, help_text='Select the connected event, if you want to make thread of events', on_delete=models.SET_NULL)


    @property
    def get_comments(self):
        return self.comments.all().order_by('-id')

    def get_status(self):
        return self.status == "Completed"


    def __str__(self):
        return f'{self.event_activity_type} - {self.date}'


class Comments(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    comment = models.TextField()
    event = models.ForeignKey(Event, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username