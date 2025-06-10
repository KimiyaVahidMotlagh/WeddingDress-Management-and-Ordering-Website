from django.shortcuts import render, redirect
from .forms import MeasurementForm
from .models import Measurement
from dresses.models import Dress

def submit_measurements(request):
    if request.method == 'POST':
        form = MeasurementForm(request.POST)
        if form.is_valid():
            measurement = form.save(commit=False)
            measurement.user = request.user
            measurement.save()
            return redirect('show_recommendations')
    else:
        form = MeasurementForm()
    return render(request, 'submit_measurements.html', {'form': form})

def show_recommendations(request):
    # Placeholder mock recommendation logic
    dresses = Dress.objects.filter(status='ready')[:3]
    return render(request, 'recommendations.html', {'dresses': dresses})
