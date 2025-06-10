from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import homepage
from bookings.views import my_bookings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('recommendation/', include('recommendation.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('bookings/', include('bookings.urls')),
    path('my/', my_bookings, name='my_bookings'),
    path('', homepage, name='homepage'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)