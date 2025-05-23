from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('jobs/', include('jobs.urls')),
    path('jokes/', include('jokes.urls')),
    path('', include('pages.urls')),
]
