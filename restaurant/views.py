from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponseRedirect
from django.urls import reverse


from .models import Bookings
from .forms import BookingForm
from datetime import datetime
import json


def home(request):
    return render(request, 'index.html', {})


def about(request):
    return render(request, 'about.html', {})


def reservations(request):
    return render(request, 'bookings.html', {
        'bookings': Bookings.objects.all()
    })


def bookings(request, id):
    booking = Bookings.objects.get(pk=id)
    return HttpResponseRedirect(reverse('reservations'))


def book(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            new_first_name = form.cleaned_data['first_name']
            new_last_name = form.cleaned_data['last_name']
            new_email = form.cleaned_data['email']
            new_phone = form.cleaned_data['phone']
            new_reservation_date = form.cleaned_data['reservation_date']
            new_reservation_slot = form.cleaned_data['reservation_slot']

            new_client = Bookings(
                first_name=new_first_name,
                last_name=new_last_name,
                email=new_email,
                phone=new_phone,
                reservation_date=new_reservation_date,
                reservation_slot=new_reservation_slot
            )
            new_client.save()
            return render(request, 'book.html', {
                'form': BookingForm(),
                'success': True
            })
    else:
        form = BookingForm()
    return render(request, 'book.html', {
        'form': BookingForm()
    })


def edit(request, id):
    if request.method == 'POST':
        booking = Bookings.objects.get(pk=id)
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return render(request, 'edit.html', {
                'form': form,
                'success': True
            })
    else:
        booking = Bookings.objects.get(pk=id)
        form = BookingForm(instance=booking)
    return render(request, 'edit.html', {
        'form': form
    })


def delete(request, id):
    if request.method == 'POST':
        booking = Bookings.objects.get(pk=id)
        booking.delete()
    return HttpResponseRedirect(reverse('reservations'))
