"""
Test for user APIs
"""

from django.urls import reverse
from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')

def create_user(**params):
    """Creating and return a new user."""
    return get_user_model().objects.create(**params)

# tests for api requests where authentication not needed, APIs like register, etc.
class PublicApiForUserTests(TestCase):
    """Tests public API requests"""
    
    def setUp(self) -> None:
        self.client = APIClient()
        
    def test_user_creation_successful(self):
        """Test user creation."""
        payload = {
            "email":"test@example.com",
            "password":"test@123",
            "name":"Test",
        }
        res = self.client.post(CREATE_USER_URL, payload)
        # print(res)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)
        
    # we will now get a clean empty db, for every test case.    
    def test_same_email_user_creation_failure(self):
        """Test user creation for failure if same email is used."""
        payload = {
            "email":"test@example.com",
            "password":"test@123",
            "name":"Test",
        }
        user = create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)   # if validation fails from serializer, it throws 400.
    
    
    def test_password_length_too_short_error(self):
        """Test that an error is returned if password is too short"""
        payload = {
            "email":"test@example.com",
            "password":"te",
        }
        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        
        user_exists = get_user_model().objects.filter(
            email=payload["email"]
        ).exists()
        self.assertFalse(user_exists)
        