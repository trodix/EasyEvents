from django.db import models


class Event(models.Model):
    title = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    address_details = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class EventDate(models.Model):
    event_date = models.DateTimeField()
    event = models.ForeignKey(to=Event, on_delete=models.CASCADE, related_name='event_dates')

    def __str__(self):
        return self.event_date.isoformat()


class AttendeeType(models.Model):
    name = models.CharField(max_length=100)
    event_price = models.DecimalField(max_digits=5, decimal_places=2)
    vat_rate = models.IntegerField()
    event = models.ForeignKey(to=Event, on_delete=models.CASCADE, related_name='attendee_types')

    def __str__(self):
        return self.name
