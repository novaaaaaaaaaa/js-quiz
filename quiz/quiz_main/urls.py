from django.urls import path
from . import views

app_name = 'quiz_main'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('leaderboard', views.leaderboard, name='leaderboard')
]