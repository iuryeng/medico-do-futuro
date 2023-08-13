from django.urls import path, include
from core.views import api_root

urlpatterns = [
   
   path('', api_root, name='api-root'),
    
]
