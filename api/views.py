from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from api.permissions import BaseCustomPermission
from api.serializers import VkAkkSerializer
from vk_akk.models import VkAkk


class VkAkkViewSet(viewsets.ModelViewSet):
    permission_classes = [BaseCustomPermission]
    serializer_class = VkAkkSerializer

    def get_queryset(self):
        return VkAkk.objects.filter(user=self.request.user)
