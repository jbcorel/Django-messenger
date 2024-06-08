from django.shortcuts import render

def show_chats(request):
    return render(request, template_name='chats/chats.html', context={})