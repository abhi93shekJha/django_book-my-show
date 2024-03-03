from rest_framework import serializers
from ..models.Show import Show
from ..models.ShowSeat import ShowSeat
from ..models.Movie import Movie
from ..models.Hall import Hall
from ..enums.SeatStatus import SeatStatus

class ShowCreateSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Show
        fields = ['hall', 'movie']
    
        
    def create(self, validate_data):
        show = Show.objects.create(**validate_data)
        # print(show)
        
        hall = validate_data['hall']
        seats = hall.seats.all()
        # print(seats)
        for seat in seats:
            ShowSeat.objects.create(seat=seat,
                                    seat_status=SeatStatus.AVAILABLE,
                                    show=show)
            
        return show
    
class ShowListByHallSerializer(serializers.ModelSerializer):
    
    movie_name = serializers.SerializerMethodField()
    class Meta:
        model = Show
        fields = ['id', 'hall', 'movie', 'movie_name', ]
    
    def get_movie_name(self, obj):
        return obj.movie.name
    
class UpdateRetrieveDestroyShowSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Show
        fields = ['hall', 'movie', ]
     
        