from django.db import models
from .BaseModel import BaseModel
from .Hall import Hall
from .Movie import Movie

class Show(BaseModel):
    
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='shows')
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    