from django.contrib import admin
from .models import Booking, BookingTime


class BookingAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'phone_number',
        'date',
        'time',
        'order',
    )


class BookingTimeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


admin.site.register(Booking, BookingAdmin)
admin.site.register(BookingTime, BookingTimeAdmin)
