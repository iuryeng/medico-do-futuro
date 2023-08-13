from django.contrib import admin
from django.urls import include, path

from core.views import api_root

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pacientes/', include('pacientes.urls')),
    #path('', include('dashboard.urls')),
    path('api/', include('core.urls')),
]
