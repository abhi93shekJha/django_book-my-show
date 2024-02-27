from django.urls import path
from .views.TheaterView import TheaterView

urlpatterns = [
    path('theater/', TheaterView.as_view(), name="create_theater"),
]
