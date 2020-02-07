from django.urls import path

from .views import (OrderSummaryView, add_to_cart, add_single_to_cart, event_detail,
                    event_detail_variation, event_list, remove_from_cart, remove_single_from_cart)

app_name = 'app'

urlpatterns = [
    path('', event_list, name='events-list'),
    path('details/<id>/', event_detail, name='event-detail'),
    path('variation/<id>/', event_detail_variation,
         name='event-detail-variation'),
    path('add-to-cart/<id>/', add_to_cart, name='add-to-cart'),
    path('add-single-to-cart/<id>/', add_single_to_cart, name='add-single-to-cart'),
    path('remove-from-cart/<id>/', remove_from_cart, name='remove-from-cart'),
    path('remove-single-from-cart/<id>/', remove_single_from_cart, name='remove-single-from-cart'),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path('', OrderSummaryView.as_view(), name='checkout')
]
