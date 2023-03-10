# Generated by Django 4.1.6 on 2023-02-11 12:35

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ticketBooking', '0018_bookings'),
    ]

    operations = [
        migrations.RenameField(
            model_name='shows',
            old_name='Show_time',
            new_name='From_time',
        ),
        migrations.AddField(
            model_name='shows',
            name='M_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='ticketBooking.movies'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shows',
            name='To_time',
            field=models.TimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
