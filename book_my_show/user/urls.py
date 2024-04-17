from django.urls import path
from user import views


# this will help use reverse('user:create') in tests module. 'user:create' create in this parameter is coming from name='create' inside path below
app_name = 'user'

urlpatterns = [
    path('create/', view=views.UserView.as_view(), name='create'),
]
