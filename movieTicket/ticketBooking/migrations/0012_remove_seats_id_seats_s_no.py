# Generated by Django 4.1.6 on 2023-02-10 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketBooking', '0011_remove_seats_s_no'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='seats',
            name='id',
        ),
        migrations.AddField(
            model_name='seats',
            name='s_no',
            field=models.IntegerField(default=1, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
