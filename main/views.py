import json

from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


from main.models import (Customer, Building, Employee, Address,
                         Apartment, CashPickup, Income, Vehicle, Expense, Payroll)
from main.serializers import *


######### API Related Code ###########


class Customer(viewsets.GenericViewSet,
               mixins.ListModelMixin,
               mixins.CreateModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               mixins.RetrieveModelMixin):

    permission_classes = (IsAuthenticated,)
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class Building(viewsets.GenericViewSet,
               mixins.ListModelMixin,
               mixins.CreateModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               mixins.RetrieveModelMixin):

    permission_classes = (IsAuthenticated,)
    queryset = Building.objects.all()
    serializer_class = BuildingSerializer

    def get_queryset(self):
        user = self.request.user
        queryset = self.queryset.filter(user=user)

        return queryset

    def create(self, request, *arg, **kwargs):
        user = self.request.user
        queryset = self.queryset.filter(user=user)

        print(user.name, user.subscription_type)
        print(queryset)

        number_of_building = len(queryset) + 1

        if (user.subscription_type == 'B' and number_of_building <= 1):
            print('inside B')

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        elif (user.subscription_type == 'P' and number_of_building <= 5):
            print('inside P')

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        elif (user.subscription_type == 'E' and number_of_building <= 10):
            print('inside E')

            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

        else:
            details = """ You have reached maximum number of buildings. Please upgrade your plan to add more."""
            return Response(json.dumps(details), status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user=user)


class Apartment(viewsets.GenericViewSet,
                mixins.ListModelMixin,
                mixins.CreateModelMixin,
                mixins.UpdateModelMixin,
                mixins.DestroyModelMixin,
                mixins.RetrieveModelMixin):

    permission_classes = (IsAuthenticated,)
    queryset = Apartment.objects.all()
    serializer_class = ApartmentSerializer


class Address(viewsets.GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin,
              mixins.RetrieveModelMixin):

    permission_classes = (IsAuthenticated,)
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class Vehicle(viewsets.GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin,
              mixins.RetrieveModelMixin):

    permission_classes = (IsAuthenticated,)
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer


class Income(viewsets.GenericViewSet,
             mixins.ListModelMixin,
             mixins.CreateModelMixin,
             mixins.UpdateModelMixin,
             mixins.DestroyModelMixin,
             mixins.RetrieveModelMixin):

    permission_classes = (IsAuthenticated,)
    queryset = Income.objects.all()
    serializer_class = IncomeSerializer


class Expense(viewsets.GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin,
              mixins.RetrieveModelMixin):

    permission_classes = (IsAuthenticated,)
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class CashPickup(viewsets.GenericViewSet,
                 mixins.ListModelMixin,
                 mixins.CreateModelMixin,
                 mixins.UpdateModelMixin,
                 mixins.DestroyModelMixin,
                 mixins.RetrieveModelMixin):

    permission_classes = (IsAuthenticated,)
    queryset = CashPickup.objects.all()
    serializer_class = CashPickupSerializer


class Employee(viewsets.GenericViewSet,
               mixins.ListModelMixin,
               mixins.CreateModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               mixins.RetrieveModelMixin):

    permission_classes = (IsAuthenticated,)
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class Payroll(viewsets.GenericViewSet,
              mixins.ListModelMixin,
              mixins.CreateModelMixin,
              mixins.UpdateModelMixin,
              mixins.DestroyModelMixin,
              mixins.RetrieveModelMixin):

    permission_classes = (IsAuthenticated,)
    queryset = Payroll.objects.all()
    serializer_class = PayrollSerializer
