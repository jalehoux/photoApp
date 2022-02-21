from django.contrib import admin
from django.urls import path
from photos.views import PhotoViewSet
from django.urls import include, path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'photos', PhotoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', include(router.urls)),
]
