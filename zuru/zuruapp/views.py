from django.shortcuts import render
from django.http import Http404
from .models import Event,Booking,User,Role

# Create your views here.
def home(request):
      '''
      View root page function that returns the index page and its data
      '''
      title = 'Home | ZuruKe'
      event_list = Event.objects.all()

      return render(request,'index.html', {"title":title,"event_list":event_list})

def events(request,event_id):
      '''
      View root page function that returns the events page and its data
      '''
      try:
            title = 'Events |'
            event = Event.objects.get(id=event_id)
      except Event.DoesNotExist:
            raise Http404
      return render(request, 'events.html', {"event":event})