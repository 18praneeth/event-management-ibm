from django import forms
from django.forms import fields
from .models import CollegeName, Comments, Event
from django.utils.translation import gettext as _


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']


class GeneralEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['date', 'quarter', 'event_activity_type', 'event_activity_mode', 'technology_tracks', 'organised_by']


class SMEEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['sme_name', 'ambassodor', 'sme_notes_id', 'sme_manager_notes_id', 'sme_bu']

        labels = {
            'sme_name': _('SME Name')
        }


class CollegeForm(forms.ModelForm):
    class Meta:
        model=CollegeName
        fields='__all__'


class EventUpdateForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'