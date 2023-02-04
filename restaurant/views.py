from django.shortcuts import render
from django.core import serializers

from .models import Bookings
from .forms import BookingForm
from datetime import datetime
import json


def home(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def reservations(request):
    date = request.GET.get('date', datetime.today().date())
    bookings = Bookings.objects.all()
    booking_json = serializers.serialize('json', bookings)
    return render(request, 'bookings.html', {
        'bookings': booking_json
    })


def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {
        'form': form
    }
    return render(request, 'book.html', context)
