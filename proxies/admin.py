from django.contrib import admin

# Register your models here.
from django.contrib.admin import ModelAdmin

from proxies.models import Proxy


# admin.site.register(Proxy)

@admin.register(Proxy)
class ProxyAdmin(ModelAdmin):
    list_display = ['ip',
                    'port',
                    'login',
                    'password']
    list_filter = ['user']

