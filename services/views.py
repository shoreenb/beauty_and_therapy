from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import Booking, UserProfile
from checkout.models import Order
from django.contrib import messages
from .forms import BookingForm


def service(request, order_number):
    """
    Send service booking form
    """
    if request.method == 'POST':
        print(request.POST['name'])
        order = get_object_or_404(Order, order_number=order_number)
        user = get_object_or_404(UserProfile, user=request.user)
        form_data = {
            'order': order,
            'user_profile': user,
            'name': request.POST['name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'date': request.POST['date'],
            'time': request.POST['time'],
        }

        booking_form = BookingForm(form_data)
        if booking_form.is_valid():
            booking = booking_form.save()

        return redirect(reverse('service_success', args=[order.order_number, booking.id]))
    else:
        order = get_object_or_404(Order, order_number=order_number)
        if not order:
            messages.error(request, "You cannot book a service that you have not ordered")
            return redirect(reverse('products'))

        booking_form = BookingForm()
        template = 'services/service.html'
        context = {
            'order': order,
            'booking_form': booking_form,
        }

        return render(request, template, context)


def service_success(request, order_number, booking_id):
    """
    Handle successful service bookings
    """

    if request.method == 'GET':
        order = get_object_or_404(Order, order_number=order_number)
        user_profile = get_object_or_404(UserProfile, user=request.user)
        booking = get_object_or_404(Booking, pk=booking_id)

        profile = UserProfile.objects.get(user=request.user)
        # Attach the user's booking to the order
        booking.user_profile = profile
        booking.save()

        messages.success(request, f'Your Booking has been confirmed! \
        Your booking number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

        template = 'services/service_success.html'
        context = {
            'order': order,
            'user_profile': user_profile,
            'booking': booking,
        }

        return render(request, template, context)


def booking_history(request, order_number, booking_id):
    order = get_object_or_404(Order, order_number=order_number)
    booking = get_object_or_404(Booking, pk=booking_id)

    messages.info(request, (
        f'This is a past service booking confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'services/service_success.html'
    context = {
        'order': order,
        'from_profile': True,
        'booking': booking,
    }

    return render(request, template, context)
