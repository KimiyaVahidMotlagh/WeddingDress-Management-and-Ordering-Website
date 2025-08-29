
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import MeasurementForm
from .models import Measurement, GeneratedImage
from dresses.models import Dress
from .utils import generate_dress_image, build_prompt
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage
import io


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

def generate_recommendation(request):
    if request.method == "POST":
        body_type = request.POST.get("body_type", "hourglass")
        sleeve = request.POST.get("sleeve", "long sleeves")
        neckline = request.POST.get("neckline", "sweetheart neckline")
        bodice = request.POST.get("bodice", "structured bodice")
        skirt = request.POST.get("skirt", "A-line skirt")
        train = request.POST.get("train", "chapel train")
        structure = request.POST.get("structure", "tailored fit")

        prompt, negative = build_prompt(body_type, sleeve, neckline, bodice, skirt, train, structure)
        image = generate_dress_image(prompt, negative)

        # Save to MEDIA folder
        buf = io.BytesIO()
        image.save(buf, format="PNG")
        file_name = f"dress_{body_type}.png"
        file_path = default_storage.save(f"recommendations/{file_name}", ContentFile(buf.getvalue()))

        return render(request, "recommendations/generated.html", {
            "image_url": default_storage.url(file_path),
            "prompt": prompt
        })
    return render(request, "recommendations/form.html")


@login_required
def recommendation_view(request):
    user_images = GeneratedImage.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'recommendations/recommendation.html', {
        'user_images': user_images
    })


def generate_image_view(request):
    if request.method == 'POST':

        generated_image = your_generation_function()  # اینجا تابع generate شما

        if generated_image:
            img_buffer = io.BytesIO()
            generated_image.save(img_buffer, format='PNG')

            generated_img = GeneratedImage(
                user=request.user,
                prompt=request.POST.get('prompt', '')
            )
            generated_img.image.save(
                f'generated_{request.user.id}_{datetime.now().timestamp()}.png',
                ContentFile(img_buffer.getvalue())
            )
            generated_img.save()

            return redirect('recommendation')

    return render(request, 'recommendation/generate.html')

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

            return redirect('recommendation:show_recommendations')
        else:
            return render(request, 'recommendation/measurements.html', {'form': form})

    else:
        form = MeasurementForm()
        return render(request, 'recommendation/measurements.html', {'form': form})

@login_required
def show_recommendations(request):
    try:
        latest_measurement = Measurement.objects.filter(user=request.user).latest('created_at')
        return render(request, 'recommendation/recommendations.html', {
            'measurement': latest_measurement
        })
    except Measurement.DoesNotExist:
        return redirect('recommendation:submit_measurements')