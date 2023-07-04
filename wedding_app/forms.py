from django import forms
from .models import *

class MyEventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ('name', 'event_date', 'venue', 'description')
class MyVenueForm(forms.ModelForm):
    class Meta:
        model = Venue
        fields = ('name', 'address', 'phone', 'email_address')
