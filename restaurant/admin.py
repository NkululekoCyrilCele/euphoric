from django.contrib import admin
from .models import Bookings, Menu

admin.site.register([Bookings, Menu])
