from django.contrib import admin
from .models.Movie import Movie
from .models.City import City
from .models.Genres import Genres
from .enums.Languages import Languages
from .enums.Format import Format

# Register your models here.

admin.site.register(Movie)
admin.site.register(City)
admin.site.register(Genres)
