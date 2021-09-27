# Generated by Django 3.1.2 on 2021-09-14 02:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnssuranceCompany',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Anssurance Company Name', max_length=255, verbose_name='Name')),
                ('logo', models.ImageField(help_text='link to Anssurance Company logo', upload_to='images/anssurance_company/', verbose_name='Logo')),
                ('email', models.EmailField(help_text='Anssurance Company Email', max_length=65, unique=True, verbose_name='Email')),
                ('phone_number', models.CharField(help_text='Phone Number', max_length=15, verbose_name='Phone')),
                ('seconde_phone_number', models.CharField(help_text='Seconde Phone Number', max_length=15, verbose_name='Phone')),
                ('address', models.CharField(help_text='Anssurance Company Address', max_length=255, verbose_name='Address')),
                ('city', models.CharField(help_text='Anssurance Company City', max_length=15, verbose_name='City')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'Anssurance Company',
                'verbose_name_plural': 'Anssurance Companies',
            },
        ),
        migrations.CreateModel(
            name='AnssuranceType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anssurance_type', models.CharField(help_text='Required', max_length=255, verbose_name='Assurance Type')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('company_name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle.anssurancecompany', verbose_name='company')),
            ],
            options={
                'verbose_name': 'Anssurance Type',
                'verbose_name_plural': 'Anssurance types',
            },
        ),
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125, unique=True)),
                ('logo', models.ImageField(help_text='Make Company logo', upload_to='images/make/', verbose_name='Logo')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
            ],
            options={
                'verbose_name': 'Make',
                'verbose_name_plural': 'Makes',
            },
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serie', models.CharField(blank=True, max_length=18, null=True, unique=True, verbose_name='Vehicle Serie')),
                ('slug', models.SlugField(max_length=255, verbose_name='Slug')),
                ('matricule', models.CharField(blank=True, max_length=18, null=True, unique=True, verbose_name='Vehicle Matricule')),
                ('picture', models.ImageField(blank=True, help_text='Vehicle Picture ', null=True, upload_to='images/vehicle/', verbose_name='Vehicle Picture')),
                ('ww', models.CharField(blank=True, max_length=18, null=True, verbose_name='WWW Matricule')),
                ('entry_into_service', models.DateField(blank=True, null=True, verbose_name='Entry Into Service')),
                ('extinguisher', models.DateField(blank=True, help_text='extincteur expiratiOn date', null=True, verbose_name='Extinguisher')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
            ],
            options={
                'verbose_name': 'Vehicle',
                'verbose_name_plural': 'Vehicles',
                'ordering': ['serie', 'matricule'],
            },
        ),
        migrations.CreateModel(
            name='VehicleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125, unique=True)),
                ('gross_vehicle_weight', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Gross vehicle weight')),
                ('place_number', models.SmallIntegerField(blank=True, null=True, verbose_name='Totale Place Number')),
                ('total_length_L', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Total length L')),
                ('total_width_W', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Toltal width W')),
                ('make', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.make')),
            ],
            options={
                'verbose_name': 'Model',
                'verbose_name_plural': 'Models',
            },
        ),
        migrations.CreateModel(
            name='VehicleSpecification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('specification_name', models.CharField(help_text='Required', max_length=125, verbose_name='Specification Name')),
                ('description', models.CharField(help_text='Required', max_length=255, verbose_name='Description')),
                ('vehicle_model', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='vehicle.vehiclemodel')),
            ],
            options={
                'verbose_name': 'Modele Specification',
                'verbose_name_plural': 'Modele Specifications',
            },
        ),
        migrations.CreateModel(
            name='VehicleHome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255)),
                ('picture', models.ImageField(help_text='Vehicle Picture ', upload_to='images/vehicle/', verbose_name='Vehicle Picture')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('is_active', models.BooleanField(default=True, verbose_name='Is Active')),
                ('model', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.vehiclemodel')),
            ],
            options={
                'verbose_name': 'Home Vehicle',
                'verbose_name_plural': 'Home Vehicles',
                'ordering': ['slug'],
            },
        ),
        migrations.CreateModel(
            name='VehicleAnssuranceSpecification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effective_date', models.DateField(blank=True, null=True)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('insurance_cost', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('anssurance_document', models.ImageField(help_text='Copy of original Anssurance copy', upload_to='images/anssurance/', verbose_name='Document')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('anssurance_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.anssurancetype', verbose_name='Anssurance Type')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.vehicle', verbose_name='Vehicle')),
            ],
            options={
                'verbose_name': 'Anssurance Specification',
                'verbose_name_plural': 'Anssurance Specifications',
            },
        ),
        migrations.AddField(
            model_name='vehicle',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.vehiclemodel'),
        ),
        migrations.CreateModel(
            name='SpecialCertificat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate_name', models.CharField(help_text='Required', max_length=255, verbose_name='Special Certificat')),
                ('effective_date', models.DateField(blank=True, null=True)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('cerculation_document', models.ImageField(help_text='Copy of original Fitness document', upload_to='images/fitness/', verbose_name='Document')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.vehicle')),
            ],
            options={
                'verbose_name': 'Special Certificat',
                'verbose_name_plural': 'Special Certificats',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='ModelSpecificationValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(help_text='Vehicle specifications values (maximum of 255 carachteres)', max_length=255, verbose_name='value')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('specification', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='vehicle.vehiclespecification')),
                ('vehicle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehicle.vehicle')),
            ],
            options={
                'verbose_name': 'Vehicle Specification Value',
                'verbose_name_plural': 'Vehicle Specification Values',
            },
        ),
        migrations.CreateModel(
            name='CertificatOfCerculation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effective_date', models.DateField(blank=True, null=True)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('cerculation_document', models.ImageField(help_text='Copy of original Anssurance copy', upload_to='images/cerculation/', verbose_name='Document')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('vehicle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicle.vehicle')),
            ],
            options={
                'verbose_name': 'Cerculation Certificat',
                'verbose_name_plural': 'Cerculation Certificats',
                'ordering': ['-created_at'],
            },
        ),
        migrations.CreateModel(
            name='CertificateOfFitness',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('effective_date', models.DateField(blank=True, null=True)),
                ('expiration_date', models.DateField(blank=True, null=True)),
                ('cerculation_document', models.ImageField(help_text='Copy of original Fitness document', upload_to='images/fitness/', verbose_name='Document')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('vehicle', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicle.vehicle')),
            ],
            options={
                'verbose_name': 'Fitness Certificat',
                'verbose_name_plural': 'Fitness Certificats',
                'ordering': ['-created_at'],
            },
        ),
    ]
