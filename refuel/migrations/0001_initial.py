# Generated by Django 3.1.2 on 2021-09-15 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehicle', '0002_auto_20210915_0337'),
    ]

    operations = [
        migrations.CreateModel(
            name='Refuel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('odometer_reading', models.PositiveIntegerField(blank=True, null=True, verbose_name='Compteur KM')),
                ('fuel_quantity', models.DecimalField(decimal_places=1, max_digits=5, verbose_name='Quantitée en Litres')),
                ('fuel_unit_price', models.DecimalField(decimal_places=2, max_digits=6, verbose_name='Prix en DH')),
                ('note', models.CharField(blank=True, max_length=255, null=True, verbose_name='Remarque')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_active', models.BooleanField(default=True)),
                ('gaz_station', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicle.gazstation')),
                ('vehicle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicle.vehicle')),
            ],
            options={
                'ordering': ['gaz_station', '-created_at'],
            },
        ),
    ]
