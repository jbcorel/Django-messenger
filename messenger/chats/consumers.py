import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from .models import Message, Room
from users.models import MyUser


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        print(self.scope['url_route']['kwargs'])
        self.room_group_name = 'chat_%s' % self.room_name
        
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name,
        )
        await self.accept()
        
    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name,
        )
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        username = data['username']
        room = data['room']
        
        await self.save_message(username, room, message)
        
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat.message',
                'message': message,
                'username': username,
                'room': room,
            }
        )
        
    
    async def chat_message(self, event):
        message = event['message']
        username = event['username']
        room = event['room']
        to_send = json.dumps({
            'message': message,
            'username': username,
            'room': room})
        await self.send(text_data=to_send)
        print(to_send)
    
    @sync_to_async
    def save_message(self, user, room, content):
        user = MyUser.objects.get(username=user)
        room = Room.objects.get(slug=room)
        Message.objects.create(user=user, room=room, content=content)
