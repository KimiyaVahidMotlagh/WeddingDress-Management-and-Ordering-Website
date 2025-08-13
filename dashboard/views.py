from django.shortcuts import render
from dresses.models import Dress
from django.contrib.auth.decorators import login_required

def company_dashboard(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('admin:login')

    dresses = Dress.objects.filter(company=request.user)
    return render(request, 'company_dashboard.html', {'dresses': dresses})

@login_required
def recommendations_view(request):
    dresses = Dress.objects.all()
    return render(request, 'accounts/recommendations.html', {'dresses': dresses})
