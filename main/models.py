import os
import uuid

from django.db import models
from django.core.exceptions import ValidationError


def fpg_for_customers_files(instance, filename):
    extension = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{extension}'
    return os.path.join(f'customers_files/', filename)


class Customer(models.Model):

    CT_CHOICES = (
        ('Rent', 'Rent'),
        ('Pledge', 'Pledge'),
        ('Sale', 'Sale')
    )

    c_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    tazkera_no = models.CharField(max_length=20)
    job_title = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=15)
    no_family_members = models.CharField(max_length=2)
    email = models.EmailField()
    contract_date = models.DateField()
    contract_type = models.CharField(max_length=200, choices=CT_CHOICES)
    contract_amount = models.IntegerField()
    photo = models.FileField(upload_to=fpg_for_customers_files)
    tazkera_scan = models.FileField(upload_to=fpg_for_customers_files)
    contract_scan = models.FileField(upload_to=fpg_for_customers_files)
    grantees_letter_scan = models.FileField(upload_to=fpg_for_customers_files)

    vehicle_info = models.ForeignKey(
        'Vehicle', on_delete=models.CASCADE, related_name='customer')
    apartment = models.ForeignKey(
        'Apartment', on_delete=models.CASCADE, related_name='customer')

    def __str__(self):
        return f'{self.name} {self.last_name}, {self.job_title}, {self.phone_no}'


class Building(models.Model):

    b_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    no_of_apartments = models.IntegerField()

    address = models.ForeignKey(
        'Address', on_delete=models.CASCADE, related_name='building')

    def __str__(self):
        return f'{self.name}'


class Address(models.Model):

    a_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    province = models.CharField(max_length=200)
    district = models.CharField(max_length=200)
    region = models.CharField(max_length=200)
    street_address = models.CharField(max_length=512)

    def __str__(self):
        return f'{self.street_address}, {self.region}, {self.district}, {self.province}'


class Apartment(models.Model):

    S_CHOICES = (
        ('Occupied', 'Occupied'),
        ('Free', 'Free')
    )

    a_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    apartment_no = models.CharField(max_length=200)
    floor_no = models.IntegerField()
    no_of_rooms = models.IntegerField()
    no_of_toilets = models.IntegerField()
    status = models.CharField(max_length=200, choices=S_CHOICES)

    building = models.ForeignKey(
        'Building', on_delete=models.CASCADE, related_name='apartment')

    def __str__(self):
        return f'Apartment No: {self.apartment_no}, Status: {self.status}'


class Vehicle(models.Model):

    v_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    model = models.CharField(max_length=200)
    plate_no = models.CharField(max_length=20)
    color = models.CharField(max_length=200)
    year = models.CharField(max_length=4)

    def __str__(self):
        return f'{self.model}, {self.color}, {self.plate_no}'


class Income(models.Model):

    P_CHOICES = (
        ('Rent', 'Rent'),
        ('Services', 'Services'),
        ('Electricity', 'Electricity'),
        ('Water', 'Water'),
        ('Net Fee', 'Net Fee'),
        ('Repair', 'Repair'),
    )

    i_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    payment_month = models.CharField(max_length=200)
    payment_type = models.CharField(max_length=200, choices=P_CHOICES)
    amount = models.IntegerField()

    apartment = models.ForeignKey(
        'Apartment', on_delete=models.CASCADE, related_name='income')

    def __str__(self):
        return f'{self.amount}, {self.apartment.apartment_no}, {self.payment_month}, {self.payment_type}'


class Expense(models.Model):

    e_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=600)
    amount = models.IntegerField()

    def __str__(self):
        return f'{self.description}, {self.amount}'


class CashPickup(models.Model):

    e_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=600)
    amount = models.IntegerField()

    def __str__(self):
        return f'{self.description}, {self.amount}'


class Employee(models.Model):

    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    tazkera_no = models.CharField(max_length=20)
    job_title = models.CharField(max_length=200)
    phone_no = models.CharField(max_length=15)
    email = models.EmailField()
    contract_date = models.DateField()
    salary = models.IntegerField()
    photo = models.FileField(upload_to=fpg_for_customers_files)
    tazkera_scan = models.FileField(upload_to=fpg_for_customers_files)
    contract_scan = models.FileField(upload_to=fpg_for_customers_files)
    grantees_letter_scan = models.FileField(upload_to=fpg_for_customers_files)

    def __str__(self):
        return f'{self.name} {self.last_name}, {self.job_title}'


class Payroll(models.Model):

    p_id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=600)
    amount = models.IntegerField()

    employee = models.ForeignKey(
        'Employee', on_delete=models.CASCADE, related_name='payroll')

    def __str__(self):
        return f'{self.employee.name}, {self.employee.job_title}, {self.amount}, {self.description}'
