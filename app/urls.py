
from django.contrib import admin
from django.urls import path

from app import settings
from django.conf.urls.static import static

from cars.views import cars_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/', cars_view)

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
