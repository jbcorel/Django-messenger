from django.shortcuts import render
from .models import Room, Message
from django.contrib.auth.decorators import login_required

@login_required
def show_chats(request):
    rooms =  Room.objects.all()
    return render(request, template_name='chats/chats.html', context={'rooms': rooms})

@login_required
def room_show(request, slug):
    room_to_show = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room_to_show)
    return render(request, 'chats/room.html', {'room':room_to_show, 'messages': messages})
