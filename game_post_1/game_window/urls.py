from django.urls import path
from . import views


app_name = 'game_window'
urlpatterns = [
    path('<int:id>/', views.get_game_window, name='game'),
]
