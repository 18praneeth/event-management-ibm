from django.db import models
from django.contrib.auth.models import User
from .choice import *



class CollegeName(models.Model):
    college_name = models.CharField(max_length=500,null=True, blank=True)
    college_city = models.CharField(max_length=500,null=True, blank=True)
    college_state=models.CharField(max_length=500, null=True, blank=True)
    college_region=models.CharField(max_length=500, choices=REGION_OPTION, null=True, blank=True)
    def __str__(self):
        return self.college_name



class Event(models.Model):
    date = models.DateField(blank=True, null=True)
    quarter =  models.CharField(choices=QUARTER_OPTION, max_length=400, null=True, blank=True)
    event_activity_type = models.CharField(max_length=500, choices=EVENT_OPTION, null=True, blank=True)
    technology_tracks = models.CharField(max_length=500, choices=TRACKS_OPTION, null=True, blank=True, verbose_name='Technology Tracks')
    event_activity_mode = models.CharField(max_length=500, choices=EVENT_MODE_OPTION, null=True, blank=True)
    organised_by = models.CharField(max_length=500, choices=ORGANISED_OPTION, null=True, blank=True)
    session_topic_name = models.CharField(max_length=100, blank=True, null=True)
    session_duration = models.CharField(max_length=500, choices=SESSION_OPTION, null=True, blank=True, help_text='Session Duration in hours.')
    number_of_attendees = models.IntegerField(default=0, null=True, blank=True)
    institution_name = models.ForeignKey(CollegeName, blank=True, null=True, on_delete=models.SET_NULL)
    sme_name=models.CharField(max_length=100,null=True, blank=True)
    ambassodor = models.CharField(max_length=500, choices=BOOLEAN_OPTION, blank=True)
    sme_notes_id=models.CharField(max_length=100, verbose_name='SME Notes ID',null=True, blank=True)
    sme_manager_notes_id=models.CharField(max_length=100 , verbose_name='SME Manager Notes ID',null=True, blank=True)
    sme_bu = models.CharField(max_length=500, choices=BU_OPTION, null=True, blank=True,verbose_name='SME BU')
    ur_spoc = models.CharField(max_length=500, choices=URSPOC_OPTION, null=True, blank=True,verbose_name='UR SPOC')
    link = models.URLField(null=True, blank=True, help_text='Link of Academic Initiative Course/platform to be used from  https://ibm.biz/academic')
    status = models.CharField(max_length=500, choices=STATUS_OPTION, null=True, blank=True)
    college_category = models.CharField(max_length=500, choices=COLLEGE_OPTION, null=True, blank=True)
    publish = models.BooleanField(default=False, help_text='Tick the option if you want to publish the event')
    accepted_users = models.ManyToManyField(User, help_text='Accepted Users', related_name='accepted_user')
    rejected_users = models.ManyToManyField(User, help_text='Rejected User', related_name='rejected_user')
    assigned_user = models.ForeignKey(User, null=True, blank=True, help_text='Event Assignee', on_delete=models.SET_NULL)


    @property
    def get_comments(self):
        return self.comments.all().order_by('-id')


    def __str__(self):
        return f'{self.event_activity_type} - {self.date}'


class Comments(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    comment = models.TextField()
    event = models.ForeignKey(Event, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username