from django.contrib import admin
from api.models import (
    Event,
    EventDate,
    AttendeeType,
    Customer,
    EventOrder,
    EventTicket
)

admin.site.register(Event)
admin.site.register(EventDate)
admin.site.register(AttendeeType)
admin.site.register(Customer)
admin.site.register(EventOrder)
admin.site.register(EventTicket)
