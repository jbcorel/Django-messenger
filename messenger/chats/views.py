from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from .models import Room, Message
from .forms import RoomCreationForm 

@login_required
def show_chats(request):
    print('В показать комнаты')
    if request.method == 'POST':
        form = RoomCreationForm(request.POST)
        print('Generated a room form')
        
        if form.is_valid():
            password = form.cleaned_data.get('password')
            password = make_password(password)
            form.cleaned_data.setdefault('password', password)
            ##
            try:
                assert form.cleaned_data.get('creator_id').pk == request.user.pk
            except AssertionError:
                raise AssertionError ('Unable to create a room. Please, try again later')
            ##
            room = form.save()
            print('Saved the form')
            return JsonResponse({
                'success': True,
                'redirect_url': f'{room.slug}',
                })
        else: 
            print ('inside ELSE FORM NOT VALID')
            json_error_response = {
                'success': False,
                'form_html': render_to_string(
                    'chats/room_creation_form.html',
                    {'form': form},
                    request,
                    )
            }
            try:
                return JsonResponse(data=json_error_response)
            except:
                print ('JSON COULD NOT BE RETURNED')
    else:
        form = RoomCreationForm()
        
    rooms =  Room.objects.all()
    context_data = {
        'rooms': rooms,
        'form': form,
    }
    return render(request, template_name='chats/chats.html', context=context_data)



@login_required
def room_show(request, slug):
    room_to_show = Room.objects.get(slug=slug)
    messages = Message.objects.filter(room=room_to_show)
    return render(request, 'chats/room.html', {'room':room_to_show, 'messages': messages})


    
    