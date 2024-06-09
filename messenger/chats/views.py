from django.shortcuts import render
from .models import Room
from django.contrib.auth.decorators import login_required

@login_required
def show_chats(request):
    rooms =  Room.objects.all()
    return render(request, template_name='chats/chats.html', context={'rooms': rooms})

def room(request, slug):
    room_to_show = Room.objects.get(slug=slug)
    return render(request, 'chats/room.html', {'room':room_to_show})
