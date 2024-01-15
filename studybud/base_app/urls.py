from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_user, name='register'),
    path('profile/<str:pk>', views.user_profile, name='user_profile'),
    path('profile/update/', views.update_user, name='update_user'),
    path('logout/', views.logout_user, name='logout'),
    path('room/create', views.create_room, name='create_room'),
    path('room/update/<str:pk>', views.update_room, name='update_room'),
    path('room/delete/<str:pk>', views.delete_room, name='delete_room'),
    path('room/<str:pk>', views.room, name='room'),
    path('message/delete/<str:pk>', views.delete_message, name='delete_message'),
    path('topics/', views.topics_page, name='topics'),
    path('activities/', views.activities_page, name='activities'),
]
