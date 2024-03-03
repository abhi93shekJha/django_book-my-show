from rest_framework import serializers
from ..models import Movie
from ..models import Genres

class ShowMovieSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Movie
        exclude = ['city', ]
        
    def to_representation(self, instance):
        response_dict = super().to_representation(instance)
        genre_list = []
        for genre_id in response_dict['genres']:
            genre_list.append(Genres.objects.get(id=genre_id).genre)
        response_dict['genres'] = genre_list
        
        return response_dict