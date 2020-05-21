from django.urls import path

from users.views import login_view, logout_view, register
from vk_akk.views import VkAkkList, AddVkAkks, AuthAkk, AddAkkGroups, AkkGroupsList

app_name = 'vk_akk'
urlpatterns = [
    # path('/'),
    path('akks/', VkAkkList.as_view(), name='akks'),
    path('add_akks/', AddVkAkks.as_view(), name='add_akks'),
    path('auth_akk/', AuthAkk.as_view(), name='auth_akk'),
    path('akk_groups/', AkkGroupsList.as_view(), name='akk_groups'),
    path('add_akk_groups/', AddAkkGroups.as_view(), name='add_akk_groups')
]
