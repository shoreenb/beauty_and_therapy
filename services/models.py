from django.db import models
from profiles.models import UserProfile
from checkout.models import Order


class BookingTime(models.Model):
    """
    Provide booking time options
    """
    class Meta:
        verbose_name_plural = 'Booking Times'

    name = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class Booking(models.Model):
    """
    Maintain a log of bookings made by users
    """
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='bookings')
    name = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    date = models.DateField()
    time = models.ForeignKey(BookingTime, null=True,
                             on_delete=models.SET_NULL)
    order = models.ForeignKey(
        Order, null=True, blank=True,
        on_delete=models.CASCADE, related_name='booking_order')

    class Meta:
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return self.name
