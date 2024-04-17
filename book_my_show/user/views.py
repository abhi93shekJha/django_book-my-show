from user.serializers import UserSerializer
from rest_framework import generics

# Create your views here.
class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer
