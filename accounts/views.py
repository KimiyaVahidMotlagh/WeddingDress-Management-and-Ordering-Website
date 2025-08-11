from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomLoginForm, SignUpForm, BodyMeasurementForm, CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import BodyMeasurement


def login_view(request):
    form = CustomLoginForm(request, data=request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('post_login_redirect')
    return render(request, 'accounts/login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('post_login_redirect')
    else:
        form = SignUpForm()
    return render(request, 'accounts/signup.html', {'form': form})

@login_required
def post_login_redirect_view(request):
    user = request.user
    try:
        measurement = user.bodymeasurement
        if measurement.height is None:
            return redirect('measurements')
        else:
            return redirect('recommendations')
    except BodyMeasurement.DoesNotExist:
        return redirect('measurements')

@login_required
def measurements_view(request):
    user = request.user
    try:
        measurement = user.bodymeasurement
    except BodyMeasurement.DoesNotExist:
        measurement = None

    if request.method == 'POST':
        form = BodyMeasurementForm(request.POST, instance=measurement)
        if form.is_valid():
            bm = form.save(commit=False)
            bm.user = user

            height = form.cleaned_data.get('height')
            bust = form.cleaned_data.get('bust')
            waist = form.cleaned_data.get('waist')
            hips = form.cleaned_data.get('hips')

            if bust and waist and hips:
                if waist < bust and waist < hips:
                    bm.body_type = 'Hourglass'
                else:
                    bm.body_type = 'Other'
            bm.save()
            return redirect('body_type_result')
    else:
        form = BodyMeasurementForm(instance=measurement)

    return render(request, 'accounts/measurements.html', {'form': form})

@login_required
def body_type_result_view(request):
    user = request.user
    try:
        measurement = user.bodymeasurement
        body_type = measurement.body_type or "Unknown"
    except BodyMeasurement.DoesNotExist:
        return redirect('measurements')

    return render(request, 'accounts/body_type_result.html', {'body_type': body_type})


def logout_view(request):
    logout(request)
    return redirect('login')