"""Test our admin interface modifications."""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse

class TestAdminSite(TestCase):
    """Tests for Django Admin."""
    
    # this will always run before any of the test function runs
    def setUp(self):
        """Create user and client object."""
        self.user = get_user_model().objects.create_user(
            email="test@example.com",
            password="test123",
            name = "Test User",
        )
        
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@example.com",
            password="test123",
        )
        
        self.client = Client()
        # this will make the admin_user login, so as to further hit on admin endpoints.
        # it is same as logging in from admin interface
        self.client.force_login(self.admin_user)
        
    
    def test_users_list(self):
        """Test that users are listed on page."""    
        
        # this gives us url as /admin/core/user
        # changelist gives us list of users
        url = reverse('admin:core_user_changelist')
        
        # we will get list of users using changelist.
        res = self.client.get(url)
        
        # assertContains will check if the page contains these two values.
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
        
    def test_edit_user_page(self):
        """Test if edit user admin page works."""
        
        # this generates a url admin/core/user/{id}/change, this url will take to the page where we can edit and update this particular user fields.
        url = reverse('admin:core_user_change', args=[self.user.id])    
        res = self.client.get(url)
        
        # Ensuring the page loads
        self.assertEqual(res.status_code, 200)
    
    def test_create_user_page(self):
        """Test that the create user page works."""
        
        # url for admin/core/user/add
        url = reverse('admin:core_user_add')
        res = self.client.get(url)
        
        self.assertEqual(res.status_code, 200)
            