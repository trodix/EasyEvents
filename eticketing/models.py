from django.db import models
from django.conf import settings
from django.utils import timezone


class Event(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title


class EventDetail(models.Model):
    address = models.CharField(max_length=100)
    address_details = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    event_date = models.DateTimeField()
    event = models.ForeignKey(
        to=Event, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.address_details} - {self.address}, {self.city} {self.zipcode} {self.country}"


class Item(models.Model):
    attendee_type = models.CharField(max_length=100)
    event_price = models.DecimalField(max_digits=5, decimal_places=2)
    vat_rate = models.IntegerField()
    event_detail = models.ForeignKey(
        to=EventDetail, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.event_detail.event.title} - {self.event_detail.address_details} - {self.event_detail.event_date.strftime('%Y-%m-%d %H:%M')} - {self.attendee_type}"

    def get_ttc_price(self):
        return float(self.event_price) * float((1 + (self.vat_rate / 100)))


class UserAddress(models.Model):
    lastname = models.CharField(max_length=50)
    firstname = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50, null=True)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, null=True)
    zipcode = models.CharField(max_length=10)
    city = models.CharField(max_length=50)
    country = models.CharField(max_length=30)
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)


class OrderItem(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    quantity = models.IntegerField(default=1)
    item = models.ForeignKey(
        to=Item, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.item.event_detail.event.title} - {self.item.event_detail.address_details} - {self.item.attendee_type} - x{self.quantity}"


class Order(models.Model):
    user = models.ForeignKey(
        to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    address = models.ForeignKey(
        to=UserAddress, on_delete=models.SET_NULL, null=True)
    items = models.ManyToManyField(OrderItem)
    ordered_date = models.DateTimeField()
    ordered = models.BooleanField(default=False)
