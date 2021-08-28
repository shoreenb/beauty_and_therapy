from django.urls import path
from . import views

urlpatterns = [
    path('<slug:order_number>/', views.service, name='service'),
    path('service_success/<order_number>', views.service_success, name='service_success'),
]
