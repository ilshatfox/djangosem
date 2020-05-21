from rest_framework import serializers

from vk_akk.models import VkAkk


class VkAkkSerializer(serializers.ModelSerializer):
    class Meta:
        model = VkAkk
        fields = '__all__'