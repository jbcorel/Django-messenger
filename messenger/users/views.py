from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm
from django.contrib.auth import views as auth_views


def frontpage(request):
    return render(request, 'users/frontpage.html', {})

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            return redirect(to='frontpage')
    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})

