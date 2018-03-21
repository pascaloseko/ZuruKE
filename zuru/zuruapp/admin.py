from django.contrib import admin
from .models import Event,User,Booking,Role

# Register your models here.
admin.site.register(Event)
admin.site.register(User)
admin.site.register(Booking)
admin.site.register(Role)