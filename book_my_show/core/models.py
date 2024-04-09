"""
Database models
"""

from typing import Any
from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
    BaseUserManager
)

# this manager will be linked to custom User model
class UserManager(BaseUserManager):
    """Manager for users."""
    
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have a valid email address.")
        user = self.model(email=self.normalize_email(email), **extra_fields)   # model method will create the user for us
        user.set_password(password)
        user.save(using=self._db)   # we can specify different databases here, self._db takes the db associated with current model(User here). We can set different dbs to different models.
        
        return user
    
    def create_superuser(self, email, password):
        user = self.create_user(email, password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user

class User(AbstractBaseUser, PermissionsMixin):    # PermissionMixin is giving us is_superuser flag, for creating a superuser
    """User in the system."""
    
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)  # in future if we want to remove a user, make is_active False, but the record will persist
    is_staff = models.BooleanField(default=False)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'email'
    