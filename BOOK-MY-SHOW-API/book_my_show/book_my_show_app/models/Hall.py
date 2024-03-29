from django.db import models
from .BaseModel import BaseModel
from .Theater import Theater

class Hall(BaseModel):
    
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE, related_name="halls")
    