from rest_framework_simplejwt.views import TokenObtainPairView

from django.contrib.auth import authenticate

from rest_framework import generics, authentication
from rest_framework.permissions import IsAuthenticated

from account.serializers import MyTokenObtainPairSerializer, UserSerializer


class MyTokenObtainPairView(TokenObtainPairView):

    serializer_class = MyTokenObtainPairSerializer


class CreateUserView(generics.CreateAPIView):

    serializer_class = UserSerializer


class ManageUserView(generics.RetrieveUpdateAPIView):

    serializer_class = UserSerializer
    # authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_object(self):
        return self.request.user
