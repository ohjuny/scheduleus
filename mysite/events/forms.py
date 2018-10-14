from django import forms
from django.utils import timezone

from .models import *

# Form for a user to sign up.
class EventForm(forms.ModelForm):
    # Sets placeholders for specified fields.
    def __init__(self, *args, **kwargs):
        super(EventForm, self).__init__(*args, **kwargs)
        # Important because dates have been defined to be parsed only in this format.
        self.fields['end_datetime'].widget.attrs['placeholder'] = 'MM/DD/YY HH:MM'

    name = forms.CharField(max_length=50)
    end_datetime = forms.DateTimeField(input_formats=['%m/%d/%y %H:%M'])

    class Meta:
        model = Event
        fields = ['name', 'end_datetime']
