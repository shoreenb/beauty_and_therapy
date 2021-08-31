from django.contrib import admin

from .models import Order, BookingTime, Booking


class BookingTimeAdmin(admin.ModelAdmin):
    # Displayed fields in Admin
    list_display = (
        'name',
    )


class BookingAdmin(admin.ModelAdmin):
    # Displayed fields in Admin
    list_display = (
        'order_number'
        'name',
        'email',
        'booking_details',
        'date',
        'time'
    )
    # Bookings by earliest date
    ordering = ('date',)


admin.site.register(BookingTime, BookingTimeAdmin)
admin.site.register(Booking, BookingAdmin)
