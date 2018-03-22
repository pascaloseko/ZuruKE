from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class Role(models.Model):
      role_name = models.CharField(max_length=50)
      user = models.ForeignKey(User,on_delete=models.CASCADE)

      def __str__(self):
            return self.role_name

class Event(models.Model):
      event_name = models.CharField(max_length=70)
      image = models.ImageField(upload_to = 'gallery/',null=True,blank=True)
      location = models.CharField(max_length=70)
      cost = models.PositiveIntegerField()
      description = models.CharField(max_length=80)
      event_date = models.DateTimeField(auto_now_add=True)

      def save_event(self):
            self.save()

      @classmethod
      def events(cls, events_id):
            event = cls.objects.filter(pk=events_id)
            return event

class Booking(models.Model):
      event_id = models.ForeignKey(Event, on_delete=models.CASCADE)
      user_id = models.ForeignKey(User,on_delete=models.CASCADE)
      name = models.CharField(max_length=50)
      phone_number = models.IntegerField()
      time_stamp = models.DateTimeField(default=datetime.utcnow)

      def save_booking(self):
            self.save()

      @classmethod
      def get_booking(cls, user_id):
            booking = Booking.objects.get(pk=user_id)

      @classmethod
      def get_event(cls, pk):
            events = Event.objects.get(pk=pk)
            return events

class User(models.Model):
      email = models.EmailField()
      bookings = models.ForeignKey(Booking, on_delete=models.CASCADE)

      def __str__(self):
            return self.email