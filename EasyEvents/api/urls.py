from rest_framework import routers
from api.views import EventViewSet, EventDateViewSet, AttendeeTypeViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

router = routers.DefaultRouter()

router.register('events', EventViewSet)
router.register('events-date', EventDateViewSet)
router.register('attendee-type', AttendeeTypeViewSet)

urlpatterns = [
    path('token', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh', TokenRefreshView.as_view(), name='token_refresh')
]

urlpatterns += router.urls
