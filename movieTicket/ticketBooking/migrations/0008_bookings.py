# Generated by Django 4.1.6 on 2023-02-10 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketBooking', '0007_movies_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bookings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Movie_name', models.CharField(max_length=50)),
                ('prize', models.IntegerField()),
                ('Selected_seats', models.CharField(max_length=100)),
                ('U_name', models.CharField(default='Nikitha', max_length=30)),
            ],
        ),
    ]
