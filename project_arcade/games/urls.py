from django.conf.urls import url
from django.urls import path
from games import views

app_name = 'games'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('rock-paper-scissors/', views.rock_paper_scissors, name = 'rock_paper_scissors'),
    path('hangman/', views.hangman, name = 'hangman'),
]