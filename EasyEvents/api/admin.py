from django.contrib import admin
from api.models import Event, EventDate, AttendeeType

admin.site.register(Event)
admin.site.register(EventDate)
admin.site.register(AttendeeType)
