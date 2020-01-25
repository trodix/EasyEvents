from django.urls import path
from .views import event_list, event_detail, event_detail_variation, add_to_cart, remove_from_cart

app_name = 'app'

urlpatterns = [
    path('', event_list, name='events-list'),
    path('details/<id>/', event_detail, name='event-detail'),
    path('variation/<id>/', event_detail_variation,
         name='event-detail-variation'),
    path('add-to-cart/<id>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<id>/', remove_from_cart, name='remove-from-cart')
]
