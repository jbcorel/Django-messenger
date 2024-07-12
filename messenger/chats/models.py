from django.db import models
from users.models import MyUser
from django.utils.translation import gettext as _
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError

# class RoomPwdField (models.CharField):
#     max_length = 256
#     help_text = 'Enter Password (at least 5 characters)'
#     verbose_name = 'Password'
#     blank = False
   
    
#     def validate(self, value):
#         super().validate()
#         if not value:
#             raise ValidationError('Password must be set')
#         if len(value) < 5:
#             raise ValidationError('Password must contain at least 5 characters')
class RoomPwdField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs['max_length'] = 256
        kwargs['help_text'] = 'Enter Password (at least 5 characters)'
        kwargs['verbose_name'] = 'Password'
        kwargs['blank'] = False
        super().__init__(*args, **kwargs)
    
    def validate(self, value, model_instance):
        super().validate(value, model_instance)
        if not value:
            raise ValidationError('Password must be set')
        if len(value) < 5:
            raise ValidationError('Password must contain at least 5 characters')
        

class Room (models.Model):
    name = models.CharField(max_length=100, verbose_name='Room name')
    slug = models.SlugField(
        unique=True, 
        verbose_name='Slug', 
        help_text='Enter the name that you want to be appended to the link (e.g. chats/your_chat_slug)',
        )
    password = RoomPwdField()
    creator_id = models.ForeignKey(
        MyUser,
        related_name='created_rooms', 
        on_delete=models.SET(0),
        )
    
    # members = models.ManyToManyField(
    #     MyUser,
    #     related_name='rooms',
    #     db_column='members',
    # )
    
    def checkPassword(self, password):
        inputPassword = make_password(password)
        return check_password(inputPassword, self.password)
    
    def __str__ (self):
        return self.name

class Message(models.Model):
    content = models.TextField()
    room = models.ForeignKey(Room, related_name='messages', on_delete=models.CASCADE)
    user = models.ForeignKey(MyUser, related_name='messages', on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('timestamp',)