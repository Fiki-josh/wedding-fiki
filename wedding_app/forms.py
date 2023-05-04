from django import forms
from .models import Event

class MyEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue', 'description')
