from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
      '''
      View root page function that returns the index page and its data
      '''
      title = 'Home | ZuruKe'
      events = Event.query.all()
      return render('index.html', {"title":title,"events":events})