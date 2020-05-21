from django.urls import path

from api.views import VkAkkViewSet
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'api'
router = DefaultRouter()
router.register(r'vk_akks', VkAkkViewSet, basename='vk_akks')
urlpatterns = router.urls
