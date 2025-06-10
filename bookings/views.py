from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from .models import Booking
from dresses.models import Dress
from django.contrib.auth.decorators import login_required

@login_required
def book_dress(request, dress_id):
    dress = get_object_or_404(Dress, id=dress_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.dress = dress
            booking.save()
            return redirect('show_recommendations')  # Or another success page
    else:
        form = BookingForm()
    return render(request, 'book_dress.html', {'form': form, 'dress': dress})
