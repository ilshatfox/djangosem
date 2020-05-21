"""vk_bot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from rest_framework.permissions import IsAuthenticated

from users.views import register, IndexView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from vk_bot import settings
from django.conf.urls.static import static


docs_schema_view = get_schema_view(
    openapi.Info(
        title='API',
        default_version=f'v1',
    ), url='http://localhost:8000/docs/swagger', public=False, permission_classes=(IsAuthenticated, ),
)


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('admin/', admin.site.urls),
    path('register/', register),
    path('auth/', include('users.urls')),
    path('vk_akk/', include('vk_akk.urls')),
    path('proxies/', include('proxies.urls')),
    path('tasks/', include('tasks.urls')),
    path('vk_users/', include('vk_users.urls')),
    path('api/', include('api.urls'))
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    docs_urls = [
        path('swagger/', docs_schema_view.with_ui('swagger'), name='schema-swagger-ui'),
    ]
    urlpatterns += [path('docs/', include(docs_urls))]