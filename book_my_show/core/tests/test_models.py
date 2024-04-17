"""
Test for models
"""

from django.test import TestCase
# get_user_model will give the current default user, can either be django provided user, or a custom user. In settings.py we make custom user as default user.
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """Test models"""
    
    def test_user_creation_with_email_successful(self):
        """Test user creation"""
        email = "test@example.com"
        password = "test123"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        
        print(user)
        
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
        
    # normalization means we will lower the case for email string after @. There is an inbuilt method for this, implemented in User model    
    def test_email_is_normalized_successful(self):
        """Test for email normalization"""
        emails = [
            ("Abc.jha@Gmail.com", "Abc.jha@gmail.com"),
            ("abc.jha@GMAIL.COM", "abc.jha@gmail.com")
        ]
        
        for email in emails:
            user = get_user_model().objects.create_user(
                email=email[0]
            )
            self.assertEqual(user.email, email[1])
            
    def test_new_user_without_email_raises_error(self):
        """Test that creating a user without email raises ValueError."""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('')
    
    def test_creating_superuser_successful(self):
        email = "abc@example.com"   # example.com has been reserved for testing.
        password = "test@123"
        superuser = get_user_model().objects.create_superuser(email, password)
        
        self.assertEqual(email, superuser.email)
        self.assertTrue(superuser.is_superuser)
        