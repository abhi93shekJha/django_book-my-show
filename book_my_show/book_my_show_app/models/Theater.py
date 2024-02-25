from django.db import models
from .BaseModel import BaseModel
from .City import City

class Theater(BaseModel):
    
    name = models.CharField(max_length=255)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='theaters')
    