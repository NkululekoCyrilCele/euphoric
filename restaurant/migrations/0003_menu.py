# Generated by Django 4.1.6 on 2023-02-04 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_bookings_reservation_date_bookings_reservation_slot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('item_price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('item_description', models.TextField(default='', max_length=1000)),
                ('item_in_stock', models.IntegerField()),
            ],
        ),
    ]
