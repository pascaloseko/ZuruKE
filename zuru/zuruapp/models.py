from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.
class User(models.Model):
      email = models.EmailField()
      bookings = models.ForeignKey()

      def __str__(self):
            return self.email

class Role(models.Model):
      role_name = models.CharField(max_length=50)
      user = models.ForeignKey()

      def __str__(self):
            return self.role_name

class Booking(models.Model):
      event_id = models.ForeignKey()
      user_id = models.ForeignKey()
      name = models.CharField(max_length=50)
      phone_number = models.IntegerField()
      time_stamp = models.DateTimeField(default=datetime.utcnow)

      def save_booking(self):
            self.save()

      @classmethod
      def get_booking(cls, user_id):
            booking = Booking.objects.get(pk=user_id)

class Event(models.Model):
      event_name = models.CharField(max_length=70)
      location = models.CharField(max_length=70)
      cost = models.PositiveIntegerField()
      description = models.CharField(max_length=80)
      date = models.DateTimeField(auto_now_add=True)

      def save_event(self):
            self.save()

      @classmethod
      def get_event(cls, pk):
            events = Event.objects.get(pk=pk)
            return events