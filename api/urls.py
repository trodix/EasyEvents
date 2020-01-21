from rest_framework import routers
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from api.views import (
    EventViewSet,
    EventDateViewSet,
    AttendeeTypeViewSet,
    CustomerViewSet,
    EventOrderViewSet,
    EventTicketViewSet
)

router = routers.DefaultRouter()

router.register('events', EventViewSet)
router.register('events-date', EventDateViewSet)
router.register('attendee-type', AttendeeTypeViewSet)
router.register('customer', CustomerViewSet)
router.register('event-order', EventOrderViewSet)
router.register('event-ticket', EventTicketViewSet)

urlpatterns = [
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]

urlpatterns += router.urls
