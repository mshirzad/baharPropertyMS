from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from account import views


urlpatterns = [
    path('token/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('myAccount/', views.ManageUserView.as_view(), name='my_account'),
    path('register/', views.CreateUserView.as_view(), name='register'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
