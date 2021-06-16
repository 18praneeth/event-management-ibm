from django import forms
from django.forms import fields
from .models import CollegeName, Comments, Event
from django.utils.translation import gettext as _


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['publish', 'accepted_users', 'rejected_users', 'assigned_user']


class CollegeForm(forms.ModelForm):
    class Meta:
        model=CollegeName
        fields='__all__'


class EventUpdateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'

