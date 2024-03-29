from django.db import models
from .BaseModel import BaseModel
from ..enums import Genre

class Genres(BaseModel):
    
    genre = models.CharField(max_length=20, choices=[(g.name, g.value) for g in Genre.Genre], unique=True)