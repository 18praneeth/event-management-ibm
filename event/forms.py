from django import forms
from django.forms import fields
from .models import CollegeName, Comments, Event, SMEProfile
from django.utils.translation import gettext as _
from django.forms.widgets import CheckboxSelectMultiple


class SMEForm(forms.ModelForm):
    class Meta:
        model = SMEProfile
        exclude = ['user']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['organised_by', 'publish', 'accepted_users', 'assigned_user']


class CollegeForm(forms.ModelForm):
    class Meta:
        model=CollegeName
        fields='__all__'


class EventUpdateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


class EventAssignForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['assigned_user']

    def __init__(self, *args, **kwargs):
        super(EventAssignForm, self).__init__(*args, **kwargs)
        self.fields["assigned_user"].widget = CheckboxSelectMultiple()

