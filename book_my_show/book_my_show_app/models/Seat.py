from django.db import models
from .BaseModel import BaseModel
from .Hall import Hall
from ..enums import SeatType as ST

class Seat(BaseModel):
    
    seat_type = models.CharField(max_length = 20, choices=[(type.name, type.value) for type in ST.SeatType])
    seat_name = models.CharField(max_length=50, blank=True)
    hall = models.ForeignKey(Hall, on_delete=models.CASCADE, related_name='seats')
    is_popular = models.BooleanField(default=False)
    