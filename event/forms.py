from django import forms
from django.db.models import fields
from .models import CollegeName, Comments, Event, Smeprofile
from django.utils.translation import gettext as _
from django.forms.widgets import CheckboxSelectMultiple
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class SMEForm(forms.ModelForm):
    class Meta:
        model = Smeprofile
        exclude = ['user']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']


class EventCreateForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = ['organised_by', 'publish', 'accepted_users', 'assigned_user']
        labels = {
            'date': _('Event Date')
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('date', css_class='form-group col'),
                Column('event_activity_type', css_class='form-group col'),
                Column('technology_tracks', css_class='form-group col'),
                css_class='row'
            ),
            Row(
                Column('event_activity_mode', css_class='form-group col'),
                Column('session_duration', css_class='form-group col'),
                Column('number_of_attendees', css_class='form-group col'),
                css_class='row'
            ), 
            Row(
                Column('session_topic_name', css_class='form-group col'),
                Column('institution_name', css_class='form-group col'),
                css_class='row'
            ), 
            Row(
                Column('link', css_class='form-group col'),
                Column('ur_spoc', css_class='form-group col'),
                css_class='row'
            ),
             Row(
                Column('signup_by', css_class='form-group col'),
                Column('status', css_class='form-group col'),
                css_class='row'
            ), 
            Row(
                Column('college_category', css_class='form-group col'),
                Column('connected_event', css_class='form-group col'),
                css_class='row'
            ),
            Submit('submit', 'Create Event', css_class='mt-2 btn-block')
        )


class CollegeForm(forms.ModelForm):
    class Meta:
        model=CollegeName
        fields='__all__'


class EventUpdateForm(forms.ModelForm):
    class Meta:
        model = Event
        exclude = [ 'publish','accepted_users','assigned_user']


class EventAssignForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['assigned_user']

    def __init__(self, *args, **kwargs):
        super(EventAssignForm, self).__init__(*args, **kwargs)
        self.fields["assigned_user"].widget = CheckboxSelectMultiple()


class EventUpdateFormUser(forms.ModelForm):
    class Meta:
        model = Event
        fields = [ 'session_duration','number_of_attendees','link']

