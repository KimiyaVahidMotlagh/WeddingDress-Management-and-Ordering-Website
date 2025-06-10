from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

def homepage(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('/admin/')
        elif request.user.is_staff:
            return redirect('company_dashboard')
        else:
            return redirect('show_recommendations')
    return render(request, 'home.html')
