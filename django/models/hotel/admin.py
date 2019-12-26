from django.contrib import admin
from .models import Venue, Event, MyclubUser
# Register your models here.

@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    pass

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    pass

@admin.register(MyclubUser)
class MyclubUserAdmin(admin.ModelAdmin):
    pass

