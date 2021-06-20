from django import forms


class RangeRequestForm(forms.Form):
    start = forms.DateField(label="Start Date")
    end = forms.DateField(label="End Date")