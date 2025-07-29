from django.urls import path
from . import views


urlpatterns = [
    path('', views.main, name = "main"),
    path('players/', views.players, name ='players'),
    path('players/details/<int:id>', views.details, name = 'details'),
    path('staff/', views.staff, name = 'staff'),
    path('teams/', views.team, name = 'teams'), 
    path('user-dropdown/', views.user_dropdown, name = 'user_dropdown'),
]