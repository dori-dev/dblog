"""dblog URL Configuration
"""
from django.conf import settings
from django.conf .urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('', include('blog.urls')),
    path('api-auth/', include('rest_framework.urls')),
]

# for development
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
    urlpatterns += static(
        'contact/static/',
        document_root=settings.STATIC_ROOT,
    )
    urlpatterns += static(
        'about/static/',
        document_root=settings.STATIC_ROOT,
    )
