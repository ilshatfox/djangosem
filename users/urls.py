from django.urls import path, re_path

from users.views import login_view, logout_view, register, confirm, forgot, reset

urlpatterns = [
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
    re_path(r'confirm/(?P<code>[^/]+)/$', confirm, name='confirm'),
    path('forgot/', forgot, name='forgot'),
    re_path(r'reset/(?P<code>[^/]+)/$', reset, name='reset')
]
