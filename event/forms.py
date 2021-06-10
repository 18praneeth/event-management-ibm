from django import forms


class CommentForm(forms.Form):
    comment = forms.CharField(label='Your Comment', max_length=500, widget=forms.Textarea, help_text='Please input your comment')
    date = forms.DateField()
