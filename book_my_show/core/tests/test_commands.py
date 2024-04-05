"""
Test custom Django management commands.
"""
# mock the behaviour of the database, patch is used to mock behaviours of an object
from unittest.mock import patch

# OperationalError is thrown when we try to connect to db before db is ready
from psycopg2 import OperationalError as Psycopg2Error

# allows us to call a command, we will call our command that we are testing
from django.core.management import call_command
from django.db.utils import OperationalError   # thrown by database
from django.test import SimpleTestCase  # base test class for testing whithout using database

# when we run command using "python manage.py mycommand", first check method runs (where we check prerequisite, system check etc.) and then 
# handle method is run. We override handle and write our logic for creating custom commands
@patch('core.management.commands.wait_for_db.Command.check') # mocking check method inside our Command class (taking from BaseCommand) inside wait_for_db module
class CommandTests(SimpleTestCase):
    """Test commands."""
    
    def test_wait_for_db_ready(self, patched_check):  # check method will be received in patched_check parameter
        """Test waiting for database if database ready."""
        patched_check.return_value = True
        
        call_command('wait_for_db')  # calls this command
        
        # this checks if the check method that we have mocked is called correctly.
        patched_check.assert_called_once_with(databases=['default'])
        
    # @patch('time.sleep') can have multiple patches
    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_check): # arguement order matters for patches, according to low level patch to top level patches
        """Test, waiting for database, when getting Operational error"""
        
        # side effect helps throw exception, since we are passing exception
        # If we would have passed boolean, our mocking object returns a boolean, just like return_value used above
        # this has been implemented behind the scene
        patched_check.side_effect = [Psycopg2Error]*2 + [OperationalError]*3 + [True]
        # both the above errors are created at different stages, former when Pyscopg2 not ready and latter, when db is not setup
        
        call_command('wait_for_db')
        
        # calling the mocked check method 6 times.
        self.assertEqual(patched_check.call_count, 6)
        patched_check.assert_called_with(databases=['default'])
    