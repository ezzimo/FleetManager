# Generated by Django 3.1.2 on 2021-10-03 01:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('refuel', '0004_auto_20210918_0104'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='fuelconsumption',
            options={'ordering': ['-created_at', 'vehicle']},
        ),
        migrations.AlterModelOptions(
            name='refuel',
            options={'get_latest_by': 'created_at', 'ordering': ['gaz_station', '-created_at']},
        ),
    ]