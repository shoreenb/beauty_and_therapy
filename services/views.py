from django.shortcuts import render

from .models import Booking, BookingTime, UserProfile


def service(request):
    """
    Display the user's booking details
    """
    template = 'services/service.html'
    context = {}

    return render(request, template, context)