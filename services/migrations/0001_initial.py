# Generated by Django 3.2.6 on 2021-08-27 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('checkout', '0004_order_user_profile'),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('friendly_name', models.CharField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name_plural': 'Booking Times',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='booking_order', to='checkout.order')),
                ('time', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.bookingtime')),
                ('user_profile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bookings', to='profiles.userprofile')),
            ],
            options={
                'verbose_name_plural': 'Bookings',
            },
        ),
    ]