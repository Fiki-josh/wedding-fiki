from django.shortcuts import render
from .forms import MyEventForm
from django.http import HttpResponse
from .models import *
# from django.template import loader

context_dictionary = {'cars' : 'Ford, Ferrari, Mustang, Range Rover, Tesla'}

def home(request):
     return render(request,'Wedding_website/index.html',context_dictionary)
def gallery(request):
     instance = Venue.objects.all()
     context = {
          'instance': instance,
     }
     return render(request,'Wedding_website/gallery.html',context)
def contact(request):
     return render(request,'Wedding_website/contact.html',context_dictionary)
def venue(request,id):
     venue = Venue.objects.get(id=id)
     context = {
          'venue': venue,
     }
     return render(request,'Wedding_website/venue.html',context)
def events(request):
     event = Event.objects.all()
     if request.method == 'POST':
        form = MyEventForm(request.POST)
        if form.is_valid():
            form.save()
          #   return redirect('myevent_list')
     else:
          form = MyEventForm()
     context = {   
        'events': event, 
        'form': form
    }
     return render(request,'Wedding_website/events.html',context)
# Create your views here.
