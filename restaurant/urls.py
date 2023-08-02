from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('reservations/', views.reservations, name='reservations'),
    path('book/', views.book, name='book'),
    path('bookings/<int:id>/', views.bookings),
    path('edit/<int:id>/', views.edit, name='edit'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('menu/', views.menu, name='menu'),
    path('display_menu_item/', views.display_menu_item, name='display_menu_item'),
]
