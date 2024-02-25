from django.db import models
from .BaseModel import BaseModel
from .Genres import Genres
from .City import City
from ..enums import Languages as L, Genre as G, Format as F

class Movie(BaseModel):
    
    name = models.CharField(max_length=255)
    language = models.CharField(max_length=20, choices=[(l.name, l.value) for l in L.Languages])
    genres = models.ManyToManyField(Genres, related_name='movies')
    format = models.CharField(max_length=20, choices=[(f.name, f.value) for f in F.Format])
    
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING, related_name = "movies")
    