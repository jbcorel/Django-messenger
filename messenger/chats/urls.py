from django.urls import path
from . import views 

urlpatterns = [
    path('', views.show_chats, name='show_chats'),
    
]