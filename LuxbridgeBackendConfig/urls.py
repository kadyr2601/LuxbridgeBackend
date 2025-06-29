from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/other/', include('other.urls')),
    path('api/homepage/', include('homepage.urls')),
    path('api/about/', include('about.urls')),
    path('api/property/', include('properties.urls')),
    path('api/projects/', include('projects.urls')),
    path('api/careers/', include('careers.urls')),
    path('api/services/', include('services.urls')),
    path('api/blog/', include('blog.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
