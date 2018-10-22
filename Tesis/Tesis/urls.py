<<<<<<< HEAD
"""Tesis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
#from backend.admin import carga_masiva
#from django.config.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('carga-masiva/', carga_masiva.urls),
    #path(r'^rs',include ('backend.urls')),
    #url(r'^rs',include ('backend.urls')),
]
=======
"""Tesis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
#API
from django.conf import settings
from rest_framework.authtoken import views 
from django.conf.urls import url, include

urlpatterns = [
    url(r'api/v1/', include(('backend.urls', 'backend'), namespace='backend')),
    path('admin/', admin.site.urls)
]

urlpatterns += [
    url(r'^api/v1/auth', include('rest_framework.urls', namespace='rest_framework'))
]
>>>>>>> d52a33efb512735425f940ba06297e9d2726dffb
