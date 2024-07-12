from django.shortcuts import render, redirect
from django.conf import settings 
from .forms import UserCreationForm
from .tasks import sendMailToNewUser

def frontpage(request):
    return render(request, 'users/frontpage.html', {})

def signup(request):
    if request.user.is_authenticated:
        return redirect(to=settings.LOGIN_REDIRECT_URL)
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            sendMailToNewUser.delay_on_commit(user.pk)
            return redirect(to='users:login')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})
