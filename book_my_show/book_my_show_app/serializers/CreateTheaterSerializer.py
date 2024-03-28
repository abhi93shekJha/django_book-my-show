from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from ..models.Theater import Theater
from ..models.Hall import Hall
from ..models.Seat import Seat
from .ShowSerializer import UpdateRetrieveDestroyShowSerializer
from ..models.Show import Show


class SeatSectionSerializer(ModelSerializer):
    number_of_seats = serializers.IntegerField()
    class Meta:
        model = Seat
        fields = ['number_of_seats', 'seat_type']


class SeatSerializer(serializers.Serializer):
    number_of_sections = serializers.IntegerField(write_only=True)
    sections = SeatSectionSerializer(many=True, write_only=True)


class HallSerializer(serializers.Serializer):
    seats = SeatSerializer()


class ShowTheaterSerializer(ModelSerializer):
    
    class Meta:
        model = Theater
        fields = '__all__'


class CreateTheaterSerializer(ModelSerializer):
    
    city_id = serializers.IntegerField()
    halls = HallSerializer(many=True)
    
    class Meta:
        model = Theater
        fields = ['city_id', 'name', 'halls', ]
        
    def create(self, validate_data):
        halls_list = validate_data.pop('halls')
        
        theater_model = Theater.objects.create(**validate_data)
        
        for hall_dict in halls_list:
            hall_model = Hall.objects.create(theater=theater_model)
            seats_dict = hall_dict['seats']
            # print(seats_dict)
            no_of_sections = seats_dict['number_of_sections']
            sections_list = seats_dict['sections']
            for section_dict in sections_list:
                num_of_seats = section_dict['number_of_seats']
                seat_type = section_dict['seat_type']
                for i in range(0, num_of_seats):
                    Seat.objects.create(seat_type=seat_type, hall=hall_model)
        
        return theater_model
    
    # internally it simply serializes theater model using this serilaizer.
    # overriding to customize the response being sent to postman
    def to_representation(self, instance):
        new_instance = ShowTheaterSerializer(instance=instance)
        # print(new_instance)
        return new_instance.data



class UpdateRetrieveDestroyShowSerializer(serializers.ModelSerializer):
    time = serializers.SerializerMethodField()
    movie = serializers.SerializerMethodField()
    class Meta:
        model = Show
        fields = ['hall', 'movie', 'time']

    def get_movie(self, obj):
        return obj.movie.name

    def get_time(self, obj):
        t = obj.created_at
        print(t)
        t_object = t.time()
        
        # Extract the time components
        hour = t_object.hour
        minute = t_object.minute

        # Determine AM/PM based on the hour
        am_pm = "AM" if hour < 12 else "PM"

        # Use a formatted string literal for output
        formatted_time = f"{hour % 12}:{minute:02d} {am_pm}"

        return formatted_time


# class ShowHallShowsSerializer(ModelSerializer):
    
#     shows = UpdateRetrieveDestroyShowSerializer(many=True)
#     class Meta:
#         model = Hall
#         fields = ['id', 'shows', ]

class ShowTheatersSerializer(ModelSerializer):
    shows = serializers.SerializerMethodField()
    
    def get_shows(self, instance):
        
        movie_id = self.context.get('movie_id', '')
        all_shows = Show.objects.filter(movie=movie_id, hall__theater=instance)
        shows = UpdateRetrieveDestroyShowSerializer(all_shows, many=True)
        return shows.data
        
    class Meta:
        model = Theater
        fields = ['id', 'name', 'shows', ]
        
        