from django import forms
from django.contrib.auth import models
from django.db.models.base import Model
from django.forms import fields
from .models import Comments, Event


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = '__all__'