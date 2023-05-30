from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from main.models import *
from main.serializers import *


######### API Related Code ###########


class Customer(viewsets.GenericViewSet,
               mixins.ListModelMixin,
               mixins.CreateModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               mixins.RetrieveModelMixin):

    # permission_classes = (IsAuthenticated,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class Building(viewsets.GenericViewSet,
               mixins.ListModelMixin,
               mixins.CreateModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               mixins.RetrieveModelMixin):

    # permission_classes = (IsAuthenticated,)
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer


class Address(viewsets.GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin,
              mixins.RetrieveModelMixin):

    # permission_classes = (IsAuthenticated,)
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class Apartment(viewsets.GenericViewSet,
                mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                mixins.RetrieveModelMixin):

    # permission_classes = (IsAuthenticated,)
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer


class Vehicle(viewsets.GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin,
              mixins.RetrieveModelMixin):

    # permission_classes = (IsAuthenticated,)
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class Income(viewsets.GenericViewSet,
             mixins.ListModelMixin,
             mixins.CreateModelMixin,
             mixins.UpdateModelMixin,
             mixins.DestroyModelMixin,
             mixins.RetrieveModelMixin):

    # permission_classes = (IsAuthenticated,)
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class Expense(viewsets.GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin,
              mixins.RetrieveModelMixin):

    # permission_classes = (IsAuthenticated,)
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class CashPickup(viewsets.GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.RetrieveModelMixin):

    # permission_classes = (IsAuthenticated,)
    queryset = CashPickup.objects.all()
    serializer_class = CashPickupSerializer


class Employee(viewsets.GenericViewSet,
               mixins.ListModelMixin,
               mixins.CreateModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               mixins.RetrieveModelMixin):

    # permission_classes = (IsAuthenticated,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class Payroll(viewsets.GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin,
              mixins.RetrieveModelMixin):

    # permission_classes = (IsAuthenticated,)
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer
