from rest_framework import routers
from api.views import EventViewSet, EventDateViewSet, AttendeeTypeViewSet

router = routers.DefaultRouter()
router.register('events', EventViewSet)
router.register('events-date', EventDateViewSet)
router.register('attendee-type', AttendeeTypeViewSet)

urlpatterns = router.urls
