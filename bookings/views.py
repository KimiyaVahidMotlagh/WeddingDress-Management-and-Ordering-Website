from django.shortcuts import render, redirect, get_object_or_404
from .models import Booking
from dresses.models import Dress
from django import forms

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['booking_date']

def book_dress(request, dress_id):
    dress = get_object_or_404(Dress, id=dress_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.dress = dress
            booking.save()
            return redirect('recommendation:show_recommendations')
    else:
        form = BookingForm()
    return render(request, 'book_dress.html', {'form': form, 'dress': dress})
