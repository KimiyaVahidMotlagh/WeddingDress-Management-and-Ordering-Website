from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import CustomLoginForm

def login_view(request):
    form = CustomLoginForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/')  # Will be routed based on role at home
    return render(request, 'accounts/login.html', {'form': form})
