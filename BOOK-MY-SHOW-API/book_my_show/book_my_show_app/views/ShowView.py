from rest_framework import generics, mixins
from ..serializers.ShowSerializer import ShowCreateSerializer, UpdateRetrieveDestroyShowSerializer, ShowListByHallSerializer
from ..models.Show import Show
from rest_framework.response import Response
from rest_framework import status

class ShowView(generics.GenericAPIView, 
               mixins.CreateModelMixin,
               mixins.ListModelMixin):
    
    serializer_class = ShowCreateSerializer
    queryset = Show.objects.all()
    
    def get_queryset(self):
        hall_id = self.kwargs.get('hall_id', '')
        if hall_id:
            return Show.objects.filter(hall=hall_id)
        return self.queryset
    
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return ShowListByHallSerializer
        return self.serializer_class
    
    def get(self, request , *args, **kwargs):
        
        return self.list(request , *args, **kwargs)
        
    def post(self, request, *args, **kwargs):
        
        return self.create(request, *args, **kwargs)
        
        
        
class ShowUpdateRetrieveDestroyView(generics.RetrieveUpdateDestroyAPIView):
    
    serializer_class = UpdateRetrieveDestroyShowSerializer
    queryset = Show.objects.all()
    
    
    def perform_destroy(self, instance):
        instance.delete()
        return Response({"success":True}, status=status.HTTP_200_OK)
            
    