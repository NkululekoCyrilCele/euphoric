from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('reservations/', views.reservations, name='reservations'),
    path('book/', views.book, name='book'),
    path('<int:id>/', views.bookings, name='bookings'),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('menu/', views.menu, name='menu'),
]
