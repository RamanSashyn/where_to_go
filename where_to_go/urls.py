from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from places import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.index, name="index"),
    path("places/<int:place_id>/", views.place_details, name="place-details"),
    path("tinymce/", include("tinymce.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
