from django import forms
from django.contrib.auth import models
from django.db.models.base import Model
from django.forms import fields
from .models import CollegeName, Comments, Event
from django.utils.translation import gettext_lazy


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'


"""class SMEForm(forms.ModelForm):
    class Meta:
        model = SME
        fields = ['sme_name', 'sme_notes_id', 'sme_manager_notes_id']
        labels = {
            'sme_name': gettext_lazy('SME Name')
        }
        help_texts = {
            'sme_name': gettext_lazy('Please enter SME Name')
        }"""

class CollegeForm(forms.ModelForm):
    class Meta:
        model=CollegeName
        fields='__all__'