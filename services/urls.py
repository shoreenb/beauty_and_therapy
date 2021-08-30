from django.urls import path
from . import views

urlpatterns = [
    path('<slug:order_number>/', views.service, name='service'),
    path('service_success/<order_number>/<booking_id>', views.service_success, name='service_success'),
    path('booking_history/<order_number>', views.booking_history, name='booking_history'),
]
