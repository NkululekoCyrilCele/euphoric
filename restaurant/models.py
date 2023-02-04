from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone


class Bookings(models.Model):
    first_name = models.CharField(max_length=25)
    last_name = models.CharField(max_length=25)
    email = models.EmailField(max_length=100)
    phone = PhoneNumberField()
    reservation_date = models.DateTimeField(default=timezone.now)
    reservation_slot = models.SmallIntegerField(default=10)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Menu(models.Model):
    item_name = models.CharField(max_length=50)
    item_price = models.DecimalField(max_digits=5, decimal_places=2)
    item_description = models.TextField(max_length=1000, default='')
    item_in_stock = models.IntegerField()
    date_ordered = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.item_name
