from django.urls import path
from . import views


urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('teamdashboard/<int:team_id>/', views.team_dashboard, name ='team_dashboard'),
    path('main/', views.main, name = "main"),
    path('players/', views.players, name ='players'),
    path('players/details/<int:id>', views.details, name = 'details'),
    path('staff/', views.staff, name = 'staff'),
    path('teams/', views.team, name = 'teams'), 
    path('user-dropdown/', views.user_dropdown, name = 'user_dropdown'),
]