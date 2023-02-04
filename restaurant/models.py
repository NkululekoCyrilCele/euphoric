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
