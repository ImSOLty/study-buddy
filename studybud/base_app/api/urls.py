from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes, name='routes'),
    path('rooms/', views.get_rooms, name='routes'),
    path('rooms/<str:pk>', views.get_room, name='routes'),
]
