from django.shortcuts import render, redirect, get_object_or_404

from .models import Booking, BookingTime, UserProfile
from checkout.models import Order
from django.contrib import messages
from .forms import BookingForm


def service(request, order_number):
    """
    Service booking form
    """

    order = get_object_or_404(Order, order_number=order_number)

    template = 'services/service.html'
    context = {
        'order': order,
    }

    return render(request, template, context)


def service_success(request, order_number):
    """
    Handle successful service bookings
    """

    if request.method == 'GET':
        user = request.user
        order = get_object_or_404(Order, order_number=order_number)
        user_profile = get_object_or_404(UserProfile, user=request.user)
        booking = Booking.objects.create(
            user_profile=user_profile, 
            order=order
            )
        

        messages.success(request, f'Your Booking has been confirmed! \
        Your booking number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

        template = 'services/service_success.html'
        context = {
            'order': order,
        }

        return render(request, template, context)
