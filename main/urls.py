from django.urls import path, include

from rest_framework.routers import DefaultRouter

from main import views


router = DefaultRouter()

router.register('customers', views.Customer, basename='customer')
router.register('buildings', views.Building, basename='building')
router.register('addresses', views.Address, basename='address')
router.register('apartments', views.Apartment, basename='apartment')
router.register('vehicles', views.Vehicle, basename='vehicle')
router.register('incomes', views.Income, basename='income')
router.register('expenses', views.Expense, basename='expense')
router.register('cashPickups', views.CashPickup, basename='cashPickup')
router.register('employees', views.Employee, basename='employee')
router.register('payrolls', views.Payroll, basename='payroll')


app_name = 'main'

urlpatterns = [
    path('', include(router.urls))
]
