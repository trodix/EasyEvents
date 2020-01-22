from django.urls import path
from .views import list_events, event_detail, event_order

urlpatterns = [
    path('', list_events, name='list_events'),
    path('event/<id>', event_detail, name='event_detail'),
    path('event-order/<id>', event_order, name='event_order')
]
