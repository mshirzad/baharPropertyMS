# Generated by Django 3.2.19 on 2023-07-11 08:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import main.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('a_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('province', models.CharField(max_length=200)),
                ('district', models.CharField(max_length=200)),
                ('region', models.CharField(max_length=200)),
                ('street_address', models.CharField(max_length=512)),
            ],
        ),
        migrations.CreateModel(
            name='Apartment',
            fields=[
                ('a_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('apartment_no', models.CharField(max_length=200)),
                ('floor_no', models.IntegerField()),
                ('no_of_rooms', models.IntegerField()),
                ('no_of_toilets', models.IntegerField()),
                ('status', models.CharField(choices=[('Occupied', 'Occupied'), ('Free', 'Free')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='CashPickup',
            fields=[
                ('e_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=600)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('tazkera_no', models.CharField(max_length=20)),
                ('job_title', models.CharField(max_length=200)),
                ('phone_no', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('contract_date', models.DateField()),
                ('salary', models.IntegerField()),
                ('photo', models.FileField(upload_to=main.models.fpg_for_customers_files)),
                ('tazkera_scan', models.FileField(upload_to=main.models.fpg_for_customers_files)),
                ('contract_scan', models.FileField(upload_to=main.models.fpg_for_customers_files)),
                ('grantees_letter_scan', models.FileField(upload_to=main.models.fpg_for_customers_files)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('e_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=600)),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('v_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('model', models.CharField(max_length=200)),
                ('plate_no', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=200)),
                ('year', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('p_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('description', models.CharField(max_length=600)),
                ('amount', models.IntegerField()),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payroll', to='main.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('i_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('payment_month', models.CharField(max_length=200)),
                ('payment_type', models.CharField(choices=[('Rent', 'Rent'), ('Services', 'Services'), ('Electricity', 'Electricity'), ('Water', 'Water'), ('Net Fee', 'Net Fee'), ('Repair', 'Repair')], max_length=200)),
                ('amount', models.IntegerField()),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='income', to='main.apartment')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('c_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('tazkera_no', models.CharField(max_length=20)),
                ('job_title', models.CharField(max_length=200)),
                ('phone_no', models.CharField(max_length=15)),
                ('no_family_members', models.CharField(max_length=2)),
                ('email', models.EmailField(max_length=254)),
                ('contract_date', models.DateField()),
                ('contract_type', models.CharField(choices=[('Rent', 'Rent'), ('Pledge', 'Pledge'), ('Sale', 'Sale')], max_length=200)),
                ('contract_amount', models.IntegerField()),
                ('photo', models.FileField(upload_to=main.models.fpg_for_customers_files)),
                ('tazkera_scan', models.FileField(upload_to=main.models.fpg_for_customers_files)),
                ('contract_scan', models.FileField(upload_to=main.models.fpg_for_customers_files)),
                ('grantees_letter_scan', models.FileField(upload_to=main.models.fpg_for_customers_files)),
                ('apartment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='main.apartment')),
                ('vehicle_info', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='main.vehicle')),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('b_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('no_of_apartments', models.IntegerField()),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='building', to='main.address')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='building', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='apartment',
            name='building',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartment', to='main.building'),
        ),
        migrations.AddField(
            model_name='apartment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apartment', to=settings.AUTH_USER_MODEL),
        ),
    ]
