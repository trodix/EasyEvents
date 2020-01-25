from django.contrib import admin
from .models import Event, EventDetail, Item, OrderItem, Order

admin.site.register(Event)
admin.site.register(EventDetail)
admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order)
