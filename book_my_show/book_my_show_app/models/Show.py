from django.db import models
from .BaseModel import BaseModel
from .Hall import Hall
from .Movie import Movie

class Show(BaseModel):
    
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='shows')
    movie = models.ForeignKey(Movie, on_delete=models.DO_NOTHING)
    
    # think why? since we can have different halls but same movie, so both together should be unique
    class Meta:
        unique_together = ['hall', 'movie',]
    
    # We are adding a feature here that, same hall can show movie on a different time
    # We will have to take in start time in that case, and add the unique contraint on start_time
    # start_time = models.CharField(unique=True)
    