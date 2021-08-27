from django.db import models
from profiles.models import UserProfile
from django_countries.fields import CountryField


class BookingTime(models.Model):
    """
    Provide booking time options
    """
    class Meta:
        verbose_name_plural = 'Booking Times'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Booking(models.Model):
    """
    Maintain a log of bookings made by users
    """
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='bookings')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.CharField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=False, blank=False)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateField()
    time = models.ForeignKey('BookingTime', null=True,
                             on_delete=models.SET_NULL)

    class Meta:
        verbose_name_plural = 'Bookings'

    def __str__(self):
        return self.name