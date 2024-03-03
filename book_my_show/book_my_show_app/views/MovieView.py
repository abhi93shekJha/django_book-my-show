from rest_framework import generics, mixins
from ..models import Movie
from ..serializers.MovieSerializer import ShowMovieSerializer

class MovieView(generics.GenericAPIView, 
                mixins.ListModelMixin):
    
    queryset = Movie.objects.all()
    serializer_class = ShowMovieSerializer
    
    def get_queryset(self):
        
        city_id = self.kwargs.get('city_id', '')
        if city_id:
            queryset = Movie.objects.filter(city=city_id)
            return queryset
    
    def get(self, request, *args, **kwargs):
        
        return self.list(request, *args, **kwargs)