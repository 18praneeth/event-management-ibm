from django.db import models
from django.contrib.auth.models import User
from .choice import *



class CollegeName(models.Model):
    college_name = models.CharField(max_length=500)
    college_city = models.CharField(max_length=500)

    def __str__(self):
        return self.college_name


class Event(models.Model):
    ambassodor = models.CharField(max_length=500, choices=BOOLEAN_OPTION, blank=True)
    date = models.DateField(blank=True, null=True)
    Quarter =  models.IntegerField(default=4, null=True, blank=True)
    EventActivityType = models.CharField(max_length=500, choices=EVENT_OPTION, null=True, blank=True)
    TechnologyTracks = models.CharField(max_length=500, choices=TRACKS_OPTION, null=True, blank=True, verbose_name='Technology Tracks')
    event_activity_mode = models.CharField(max_length=500, choices=EVENT_MODE_OPTION, null=True, blank=True)
    OrganisedBy = models.CharField(max_length=500, choices=ORGANISED_OPTION, null=True, blank=True)
    session_topic_name = models.CharField(max_length=100, blank=True, null=True)
    number_of_attendees = models.IntegerField(default=0)
    institution_name = models.ForeignKey(CollegeName, blank=True, null=True, on_delete=models.SET_NULL)
    SessionDuration = models.CharField(max_length=500, choices=SESSION_OPTION, null=True, blank=True, help_text='Session Duration in hours.')
    SMEBU = models.CharField(max_length=500, choices=BU_OPTION, null=True, blank=True)
    URSPOC = models.CharField(max_length=500, choices=URSPOC_OPTION, null=True, blank=True)
    link = models.URLField(null=True, blank=True, help_text='Link of Academic Initiative Course/platform to be used from  https://ibm.biz/academic')
    Status = models.CharField(max_length=500, choices=STATUS_OPTION, null=True, blank=True)
    CollegeCategory = models.CharField(max_length=500, choices=COLLEGE_OPTION, null=True, blank=True)


    @property
    def get_comments(self):
        return self.comments.all().order_by('-id')


    # def __str__(self):
    #     return self.name


class Comments(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    comment = models.TextField()
    event = models.ForeignKey(Event, related_name='comments', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username