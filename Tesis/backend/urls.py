<<<<<<< HEAD
#from django.contrib import admin
#from django.urls import path
#from django.config.urls import url

#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path(r'^rs',include ('backend.urls')),
#]
=======
from django.conf.urls import url
from backend.views import *

urlpatterns = [
    url(r'^backend/$', ProductoList.as_view(), name='backend')
]
>>>>>>> d52a33efb512735425f940ba06297e9d2726dffb
