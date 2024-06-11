from django.db import models
from django.contrib.auth.models import User

class Room (models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

class Message(models.Model):
    content = models.TextField()
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('timestamp',)