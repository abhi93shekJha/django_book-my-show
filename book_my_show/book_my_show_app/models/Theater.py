from django.db import models
from .BaseModel import BaseModel
from .City import City

class Theater(BaseModel):
    
    name = models.CharField(max_length=255, unique=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='theaters')
    