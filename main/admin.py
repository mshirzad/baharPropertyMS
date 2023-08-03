from django.contrib import admin
from main.models import *


class CustomerAdmin(admin.ModelAdmin):
    pass


admin.site.register(Customer, CustomerAdmin)


class ApartmentAdmin(admin.ModelAdmin):
    pass


admin.site.register(Apartment, ApartmentAdmin)


class BuildingAdmin(admin.ModelAdmin):
    pass


admin.site.register(Building, BuildingAdmin)


class VehicleAdmin(admin.ModelAdmin):
    pass


admin.site.register(Vehicle, VehicleAdmin)


class AddressAdmin(admin.ModelAdmin):
    pass


admin.site.register(Address, AddressAdmin)


class IncomeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Income, IncomeAdmin)


class ExpenseAdmin(admin.ModelAdmin):
    pass


admin.site.register(Expense, ExpenseAdmin)


class CashPickupAdmin(admin.ModelAdmin):
    pass


admin.site.register(CashPickup, CashPickupAdmin)


class EmployeeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Employee, EmployeeAdmin)


class PayrollAdmin(admin.ModelAdmin):
    pass


admin.site.register(Payroll, PayrollAdmin)


admin.site.site_header = 'Bahar Property Management System'
