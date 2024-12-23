"""django_modules URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework_jwt.views import obtain_jwt_token
from django_private_chat import urls as django_private_chat_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^', include('django_modules.home.urls')),
    url(r'^', include('django_modules.reports.urls')),
    url(r'^', include('django_modules.apis.urls')),
    url(r'^', include('django_modules.crud.urls')),
    url(r'^', include('django_modules.authentication.urls')),
    url(r'^', include('django_modules.emails.urls')),
    url(r'^', include('django_modules.cache.urls')),
    url(r'^', include('django_modules.chart.urls')),
    url(r'^', include('django_modules.inlineform.urls')),
    url(r'^', include('django_modules.usercustom.urls')),
    url(r'^', include('django_modules.chat.urls')),
    url(r'^', include('django_private_chat.urls')),   
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^api-token-auth/', obtain_jwt_token),

]
