from django.urls import path
from . import views 

urlpatterns = [
    path('', views.show_chats, name='show_chats'),
    path('<slug:slug>/', views.room_show, name='room'),
    
]
