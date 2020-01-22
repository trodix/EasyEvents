from django.db import models
from django.utils import timezone
from eticketing.utils import generate_ticket_number


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=100)
    address_details = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=30)

    def __str__(self):
        return self.title


class EventDate(models.Model):
    event_date = models.DateTimeField()
    event = models.ForeignKey(
        to=Event, on_delete=models.CASCADE, related_name='event_dates')

    def __str__(self):
        return self.event_date.isoformat()


class AttendeeType(models.Model):
    name = models.CharField(max_length=100)
    event_price = models.DecimalField(max_digits=5, decimal_places=2)
    vat_rate = models.IntegerField()
    event = models.ForeignKey(
        to=Event, on_delete=models.CASCADE, related_name='attendee_types')

    def __str__(self):
        return self.event.title + ' - ' + self.name


class Customer(models.Model):
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=15, null=True)
    email = models.EmailField()
    billing_address = models.CharField(max_length=100)
    billing_zipcode = models.CharField(max_length=10)
    billing_city = models.CharField(max_length=50)
    billing_country = models.CharField(max_length=30)

    def __str__(self):
        return self.lastname + ' ' + self.firstname


class EventOrder(models.Model):
    order_date = models.DateTimeField(default=timezone.now)
    amount = models.DecimalField(max_digits=5, decimal_places=2)
    event = models.ForeignKey(
        to=Event, on_delete=models.CASCADE, related_name='event_orders')
    customer = models.ForeignKey(
        to=Customer, on_delete=models.CASCADE, related_name='event_orders')

    def __str__(self):
        return self.order_date.isoformat()


class EventTicket(models.Model):
    ticket_number = models.CharField(
        max_length=20, default=generate_ticket_number(), editable=False, unique=True)
    event = models.ForeignKey(
        to=Event, on_delete=models.CASCADE, related_name='event_tickets')
    attendee_type = models.ForeignKey(
        to=AttendeeType, on_delete=models.CASCADE, related_name='event_tickets')

    def __str__(self):
        return self.ticket_number
