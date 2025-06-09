from django.shortcuts import render, get_object_or_404, redirect
from .models import Dress, Favorite

def dress_list(request):
    dresses = Dress.objects.filter(status='ready')
    return render(request, 'dress_list.html', {'dresses': dresses})

def toggle_favorite(request, dress_id):
    dress = get_object_or_404(Dress, id=dress_id)
    favorite, created = Favorite.objects.get_or_create(user=request.user, dress=dress)
    if not created:
        favorite.delete()  # Toggle off
    return redirect('dress_list')
