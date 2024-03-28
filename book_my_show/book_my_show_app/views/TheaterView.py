from rest_framework import generics, mixins
from ..serializers.CreateTheaterSerializer import CreateTheaterSerializer, ShowTheatersSerializer
from ..models.Theater import Theater
from ..models.Hall import Hall
from ..models.Show import Show

class TheaterView(generics.GenericAPIView,
               mixins.CreateModelMixin):
    
    queryset = Theater.objects.all()
    serializer_class = CreateTheaterSerializer
    
    def post(self, request, *args, **kwargs):
        
        return self.create(request, *args, **kwargs)


class ShowTheaterByMovieView(generics.GenericAPIView,
                             mixins.ListModelMixin):
    
    queryset = Theater.objects.all()
    serializer_class = ShowTheatersSerializer
    
    def get_serializer_context(self):
        return {'movie_id':self.kwargs.get('movie_id', '')}
    
    def get(self, request, *args, **kwargs):
        # movie_id = kwargs.get('movie_id', '')
        # shows = Show.objects.filter(movie=movie_id)  # this won't run any query, until shows is used or printed somewhere
        # halls = []
        # for show in shows:
        return self.list(request, *args, **kwargs)
    