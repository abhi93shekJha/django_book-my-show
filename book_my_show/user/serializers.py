"""
Creating serializers
"""
from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=get_user_model()
        fields = ['email', 'password', 'name',]
        extra_kwargs = {'password': {'write_only':True, 'min_length': 5}}   # This will not return password in response, and will throw BAD_REQUEST when password entered is less than 5
    
    # override this method since we are using custom user and do not want default behaviour
    def create(self, validated_date):
        """create the instance of user since using custom user"""
        return get_user_model().objects.create_user(**validated_date)   # this will make the password hashed as implemented in create_user method when creating custom user model