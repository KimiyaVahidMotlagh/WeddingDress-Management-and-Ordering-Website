from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import CustomLoginForm, SignUpForm, BodyMeasurementForm, CustomUserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import BodyMeasurement
import os
from django.conf import settings
from django.core.files.storage import default_storage


def user_home_view(request):
    user = request.user

    dress_images = []
    dresses_path = os.path.join(settings.MEDIA_ROOT, 'All Dresses')

    if os.path.exists(dresses_path):
        for filename in os.listdir(dresses_path):
            if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')):
                dress_images.append({
                    'url': os.path.join(settings.MEDIA_URL, 'All Dresses', filename).replace('\\', '/'),
                    'name': os.path.splitext(filename)[0]  # حذف پسوند فایل
                })

    return render(request, 'accounts/user-home.html', {
        'dress_images': dress_images
    })

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

def post_login_redirect_view(request):
    user = request.user
    try:
        measurement = user.bodymeasurement
        if measurement and measurement.body_type:
            return redirect('user_home')
        else:
            return redirect('measurements')
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
            high_hip = form.cleaned_data.get('high_hip')
            hips = form.cleaned_data.get('hips')

            if bust and waist and hips and high_hip:
                waist_hip_ratio = waist / hips if hips else 0
                bust_hip_ratio = bust / hips if hips else 0
                waist_high_hip_ratio = waist / high_hip if high_hip else 0

                # منطق تشخیص تیپ بدنی
                if waist_hip_ratio >= 0.85 and (abs(bust - hips) < 5) and (waist >= 88):
                    bm.body_type = "Apple"
                elif waist_hip_ratio < 0.7 and bust_hip_ratio > 1.1:
                    bm.body_type = "Hourglass"
                elif waist_hip_ratio >= 0.75 and abs(bust - hips) < 5:
                    bm.body_type = "Rectangle"
                elif waist_hip_ratio > 0.8 and bust < hips:
                    bm.body_type = "Triangle"
                elif waist_hip_ratio > 0.8 and bust > hips:
                    bm.body_type = "Inverted Triangle"
                else:
                    bm.body_type = "Other"
            else:
                bm.body_type = "Incomplete data"

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

def recommendations_view(request):
    return render(request, 'recommendations/recommendation.html')

def logout_view(request):
    logout(request)
    return redirect('login')

def favorites(request):
    return render(request, 'favorites.html')

