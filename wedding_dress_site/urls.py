from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import homepage, about_view, contact_view
from bookings.views import my_bookings
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage, name='homepage'),
    path('accounts/', include('accounts.urls')),
    path('recommendation/', include('recommendation.urls')),
    path('about/', about_view, name='about'),
    path('contact/', contact_view, name='contact'),
    path('dresses/', include('dresses.urls')),
    path('bookings/', include('bookings.urls')),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

