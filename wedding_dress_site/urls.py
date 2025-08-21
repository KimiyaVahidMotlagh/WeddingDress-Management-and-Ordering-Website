from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import homepage, about_view, contact_view
from bookings.views import my_bookings
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recommendation/', include('recommendation.urls')),
    path('bookings/', include('bookings.urls')),
    path('accounts/', include('accounts.urls')),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('my/', my_bookings, name='my_bookings'),
    path('', homepage, name='homepage'),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)