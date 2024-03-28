from django.urls import path
from .views.TheaterView import TheaterView
from .views.MovieView import MovieView
from .views.ShowView import ShowView, ShowUpdateRetrieveDestroyView
from .views.TheaterView import ShowTheaterByMovieView


urlpatterns = [
    path('theater/', TheaterView.as_view(), name="create_theater"),
    path('city/<int:city_id>/movies', MovieView.as_view(), name="list_of_movies"),
    path('show', ShowView.as_view(), name="create_show"),
    path('hall/<int:hall_id>/show', ShowView.as_view(), name='get_shows_by_hall_id'),
    
    # if pk name not used, the view will throw an error, as we are using generics.RetrieveUpdateAPIView
    path('show/<int:pk>', ShowUpdateRetrieveDestroyView.as_view(), name='update and retrieve show by show_id'),
    path('movie/<int:movie_id>/shows', ShowTheaterByMovieView.as_view(), name='get shows by movie id'),

]
