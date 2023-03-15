from dj_rest_auth.views import LogoutView
from rest_framework import generics, permissions
from rest_framework.authtoken.admin import User
from . import serializers

class CustomLogoutView(LogoutView):
    permission_classes = (permissions.IsAuthenticated, )

class UserRegisterView(generics.CreateAPIView):
    qs = User.objects.all()
    serializer_class = serializers.RegisterSerializer

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserListSerializer
    permission_classes = (permissions.IsAuthenticated,)

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serialize_class = serializers.UserDetailsSerializer
    permission_classes = (permissions.IsAuthenticated,)
