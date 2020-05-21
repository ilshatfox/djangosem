from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from tasks.models import FollowTask, AkkFollowTask


@admin.register(FollowTask)
class FollowTaskAdmin(ModelAdmin):
    list_display = ['id',
                    'vk_akks_group',
                    'vk_users_group',
                    'follow_number',
                    'status',
                    'is_fast_follow']
    list_filter = ['user']


@admin.register(AkkFollowTask)
class AkkFollowTaskAdmin(ModelAdmin):
    list_display = ['id',
                    'vk_akk',
                    'complete_num',
                    'success_num']
