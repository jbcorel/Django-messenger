from .models import MyUser 
from django.contrib.auth.forms import BaseUserCreationForm 

class UserCreationForm (BaseUserCreationForm):
    class Meta:
        model = MyUser 
        fields = ('username', 'email',)