from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('reservations/', views.reservations, name='reservations'),
    path('book/', views.book, name='book'),
    # path('bookings/', views.bookings, name='bookings'),
]
