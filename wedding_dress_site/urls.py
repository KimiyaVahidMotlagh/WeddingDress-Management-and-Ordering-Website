from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from core.views import homepage
from bookings.views import my_bookings
import os

urlpatterns = [
    path('admin/', admin.site.urls),
    path('recommendation/', include('recommendation.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('bookings/', include('bookings.urls')),
    path('accounts/', include('accounts.urls')),
    path('my/', my_bookings, name='my_bookings'),
    path('', homepage, name='homepage'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=os.path.join(settings.BASE_DIR, 'static'))