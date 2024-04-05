"""
Django command to wait for the database to be available
"""
import time

from psycopg2 import OperationalError as Psycopg2OpError

from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

# we can now call command wait_for_db, using python manage.py wait_for_db
class Command(BaseCommand):
    """Django command to wait for database."""
    
    def handle(self, *args, **options):
        """ Entrypoint for command. """
        self.stdout.write('Waiting for database...')   # logging to console
        db_up = False
        while db_up is False:
            try:
                self.check(databases=['default'])   # this will check if database is available, for the default db from settings
                db_up = True
            except (Psycopg2OpError, OperationalError):
                self.stdout.write('Database unavailable, waiting 1 second...')
                time.sleep(1)
        
        self.stdout.write(self.style.SUCCESS('Database available!'))            
    