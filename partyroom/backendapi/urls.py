from django.urls import path
from .views import RoomView

# Produce the views defined in the main function under  views.py
urlpatterns = [
    path('room', RoomView.as_view()),
]