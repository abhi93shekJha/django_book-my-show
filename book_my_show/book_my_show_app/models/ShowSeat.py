from django.db import models
from .BaseModel import BaseModel
from .Seat import Seat
from .Show import Show
from ..enums import SeatStatus as SS

class ShowSeat(BaseModel):
    
    # think why not OneToOneField used instead of ForeignKey
    seat = models.ForeignKey(Seat, on_delete=models.CASCADE)
    seat_status = models.CharField(max_length=20, choices=[(status.name, status.value) for status in SS.SeatStatus])
    show = models.ForeignKey(Show, on_delete=models.CASCADE, related_name = 'show_seats')
    