# recommendation/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import MeasurementForm
from .models import Measurement
from dresses.models import Dress


@login_required
def submit_measurements(request):
    if request.method == 'POST':
        form = MeasurementForm(request.POST)
        if form.is_valid():
            measurement = form.save(commit=False)
            measurement.user = request.user

            # تشخیص body type
            bust_waist_ratio = measurement.bust / measurement.waist if measurement.waist > 0 else 0
            if bust_waist_ratio > 1.2:
                body_type = "hourglass"
            elif measurement.hips > measurement.bust:
                body_type = "pear"
            else:
                body_type = "rectangle"
            measurement.body_type = body_type
            measurement.save()

            return redirect('show_recommendations')
        else:
            return render(request, 'accounts/measurements.html', {'form': form})

    else:
        form = MeasurementForm()
        return render(request, 'accounts/measurements.html', {'form': form})


@login_required
def show_recommendations(request):
    try:
        latest_measurement = Measurement.objects.filter(user=request.user).latest('created_at')
        static_dresses = Dress.objects.all()

        return render(request, 'recommendation/recommendations.html', {
            'measurement': latest_measurement,
            'static_dresses': static_dresses
        })
    except Measurement.DoesNotExist:
        return redirect('submit_measurements')