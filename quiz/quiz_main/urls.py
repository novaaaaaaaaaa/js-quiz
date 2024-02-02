from django.urls import path
from . import views

app_name = 'quiz_main'

urlpatterns = [
    path('', views.landing, name='landing'),
    path('quiz', views.quiz, name='quiz'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
    path('score', views.score, name="score"),
]