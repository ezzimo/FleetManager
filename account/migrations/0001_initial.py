# Generated by Django 3.1.2 on 2021-09-13 00:48

import uuid

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("password", models.CharField(max_length=128, verbose_name="password")),
                ("last_login", models.DateTimeField(blank=True, null=True, verbose_name="last login")),
                (
                    "is_superuser",
                    models.BooleanField(
                        default=False,
                        help_text="Designates that this user has all permissions without explicitly assigning them.",
                        verbose_name="superuser status",
                    ),
                ),
                (
                    "user_type",
                    models.CharField(
                        choices=[("cu", "Customer"), ("ad", "Administration"), ("dr", "Driver")], max_length=2
                    ),
                ),
                ("email", models.EmailField(max_length=254, unique=True, verbose_name="Email Address")),
                ("first_name", models.CharField(max_length=150, unique=True, verbose_name="First Name")),
                ("last_name", models.CharField(max_length=150, unique=True, verbose_name="Last Name")),
                ("mobile", models.CharField(blank=True, max_length=150, verbose_name="Mobile Number")),
                ("is_active", models.BooleanField(default=False, verbose_name="Is Active")),
                ("is_staff", models.BooleanField(default=False, verbose_name="Is Staff")),
                ("is_client", models.BooleanField(default=False, verbose_name="Is Client")),
                ("is_technic", models.BooleanField(default=False, verbose_name="Is Technic")),
                ("is_exploitation", models.BooleanField(default=False, verbose_name="Is Exploitation")),
                ("is_controlor", models.BooleanField(default=False, verbose_name="Is Controlor")),
                ("is_supervisor", models.BooleanField(default=False, verbose_name="Is Supervisor")),
                ("is_planification", models.BooleanField(default=False, verbose_name="Is Planification")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Created at")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Updated at")),
                (
                    "registration_number",
                    models.PositiveSmallIntegerField(blank=True, null=True, verbose_name="Driver Registration Number"),
                ),
                ("cni", models.CharField(blank=True, max_length=8, null=True, verbose_name="National Identity Code")),
                (
                    "picture",
                    models.ImageField(
                        blank=True,
                        help_text="Driver Identity Picture",
                        null=True,
                        upload_to="images/driver/",
                        verbose_name="Driver Pic",
                    ),
                ),
                ("birth_date", models.DateField(blank=True, null=True, verbose_name="Date Birth of the Driver")),
                (
                    "birth_city",
                    models.CharField(blank=True, max_length=150, null=True, verbose_name="Birth City of the Driver"),
                ),
                (
                    "cnss_registration_number",
                    models.PositiveIntegerField(blank=True, null=True, verbose_name="CNSS Registration Number"),
                ),
                ("recruitment_date", models.DateField(blank=True, null=True)),
                (
                    "Contract_type",
                    models.CharField(
                        blank=True,
                        choices=[("Per.", "Permanent"), ("Tem.", "Temporaire")],
                        default="Per.",
                        max_length=4,
                    ),
                ),
                (
                    "rib_bank",
                    models.PositiveIntegerField(blank=True, null=True, verbose_name="RIB of the Driver Bank"),
                ),
                ("bank_address", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "driving_licence",
                    models.ImageField(
                        blank=True,
                        help_text="Driver Licence Picture",
                        null=True,
                        upload_to="images/driver_licence/",
                        verbose_name="Driver Licence",
                    ),
                ),
                (
                    "driver_licence_expiration_date",
                    models.DateField(blank=True, null=True, verbose_name="Expiration Date for Driver Licence"),
                ),
                ("glasses", models.BooleanField(default=False, verbose_name="if the Driver use Glasses")),
                (
                    "glasses_certificat",
                    models.ImageField(
                        blank=True,
                        help_text="Driver Glasses Certificat Picture",
                        null=True,
                        upload_to="images/driver_glasse_certificate/",
                        verbose_name="Driver Glasse Certificate",
                    ),
                ),
            ],
            options={
                "verbose_name": "Account",
                "verbose_name_plural": "Accounts",
            },
        ),
        migrations.CreateModel(
            name="Bank",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("bank_name", models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Region",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("region", models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name="EmployeeSalary",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                (
                    "salary",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=7, null=True, verbose_name="Employee Salary"
                    ),
                ),
                (
                    "payment_mode",
                    models.CharField(choices=[("Vir", "Virement"), ("Esp", "Especes")], default="Vir", max_length=3),
                ),
                ("is_active", models.BooleanField(default=False, verbose_name="Is Active")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Created at")),
                ("updated_at", models.DateTimeField(auto_now=True, verbose_name="Updated at")),
                (
                    "employee",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
                ),
            ],
            options={
                "verbose_name": "Salary",
                "verbose_name_plural": "Salaris",
                "ordering": ("-created_at",),
            },
        ),
        migrations.CreateModel(
            name="City",
            fields=[
                ("id", models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("city", models.CharField(max_length=128)),
                (
                    "region_id",
                    models.ForeignKey(
                        blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="account.region"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Address",
            fields=[
                ("id", models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ("address_name", models.CharField(max_length=50, verbose_name="Address Name")),
                ("phone", models.CharField(max_length=50, verbose_name="Phone Number")),
                ("postcode", models.CharField(max_length=50, verbose_name="Postcode")),
                ("address_line_1", models.CharField(max_length=255, verbose_name="Address Line 1")),
                ("address_line_2", models.CharField(max_length=255, verbose_name="Address Line 2")),
                ("town_city", models.CharField(max_length=150, verbose_name="Town/City/State")),
                ("delivery_instructions", models.CharField(max_length=255, verbose_name="Delivery Instructions")),
                ("created_at", models.DateTimeField(auto_now_add=True, verbose_name="Created at")),
                ("updated", models.DateTimeField(auto_now=True, verbose_name="Updated at")),
                ("default", models.BooleanField(default=False, verbose_name="Default")),
                (
                    "customer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="Customer",
                    ),
                ),
            ],
            options={
                "verbose_name": "Address",
                "verbose_name_plural": "Addresses",
            },
        ),
        migrations.AddField(
            model_name="user",
            name="bank_id",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="account.bank"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="city_id",
            field=models.ForeignKey(
                blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to="account.city"
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="groups",
            field=models.ManyToManyField(
                blank=True,
                help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                related_name="user_set",
                related_query_name="user",
                to="auth.Group",
                verbose_name="groups",
            ),
        ),
        migrations.AddField(
            model_name="user",
            name="user_permissions",
            field=models.ManyToManyField(
                blank=True,
                help_text="Specific permissions for this user.",
                related_name="user_set",
                related_query_name="user",
                to="auth.Permission",
                verbose_name="user permissions",
            ),
        ),
    ]
