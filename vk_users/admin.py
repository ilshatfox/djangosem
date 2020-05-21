from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from vk_users.models import VkUser, VkUsersGroup, VkFileUsers, VkNews

# admin.site.register(VkUser)
# admin.site.register(VkUsersGroup)
# admin.site.register(VkFileUsers)
# admin.site.register(VkNews)


@admin.register(VkUser)
class FollowTaskAdmin(ModelAdmin):
    list_display = ['vk_id',
                    'vk_username']


@admin.register(VkUsersGroup)
class FollowTaskAdmin(ModelAdmin):
    list_display = ['name',
                    'user']
    list_filter = ['user']


@admin.register(VkFileUsers)
class FollowTaskAdmin(ModelAdmin):
    list_display = ['filename',
                    'user']
    list_filter = ['user']


@admin.register(VkNews)
class FollowTaskAdmin(ModelAdmin):
    list_display = ['name',
                    'body']
    list_filter = ['user']
