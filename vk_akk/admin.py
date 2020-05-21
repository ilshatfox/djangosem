from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from vk_akk.models import VkAkk, UserAgent, VkAkksGroup


# admin.site.register(VkAkk)
# admin.site.register(UserAgent)
# admin.site.register(VkAkksGroup)

@admin.register(VkAkk)
class FollowTaskAdmin(ModelAdmin):
    list_display = ['login',
                    'password',
                    'vk_user_id',
                    'proxy',
                    'vk_url']
    list_filter = ['user']


@admin.register(UserAgent)
class FollowTaskAdmin(ModelAdmin):
    list_display = ['user_agent']


@admin.register(VkAkksGroup)
class FollowTaskAdmin(ModelAdmin):
    list_display = ['id',
                    'name']
    list_filter = ['user']
