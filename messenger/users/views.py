from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import UserCreationForm
from .tasks import sendMailToNewUser

def frontpage(request):
    return render(request, 'users/frontpage.html', {})

##should be for non_authenticated users only
##similar for login view
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            sendMailToNewUser.delay_on_commit(user.pk)
            print (f'PK of user dur signup= {user.pk}')
            return redirect(to='users:login')
    else:
        form = UserCreationForm()
    return render(request, 'users/signup.html', {'form': form})

