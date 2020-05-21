
from django.urls import path

from proxies.views import ProxiesList, AddProxies

app_name = 'proxies'
urlpatterns = [
    path('proxy_list/', ProxiesList.as_view(), name='proxy_list'),
    path('add_proxies/', AddProxies.as_view(), name='add_proxies')
]