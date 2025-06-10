from django.shortcuts import render
from dresses.models import Dress

def company_dashboard(request):
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect('admin:login')  # Or show a 403 page

    dresses = Dress.objects.filter(company=request.user)
    return render(request, 'company_dashboard.html', {'dresses': dresses})