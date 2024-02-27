from rest_framework import generics, mixins
from ..serializers.CreateTheaterSerializer import CreateTheaterSerializer
from ..models.Theater import Theater

class TheaterView(generics.GenericAPIView, 
               mixins.CreateModelMixin):
    
    queryset = Theater.objects.all()
    serializer_class = CreateTheaterSerializer
    
    def post(self, request, *args, **kwargs):
        
        return self.create(request, *args, **kwargs)
    