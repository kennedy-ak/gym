from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard_home, name='home'),
    path('book/', views.booking_form, name='booking_form'),
    path('booking/success/', views.booking_success, name='booking_success'),
]
