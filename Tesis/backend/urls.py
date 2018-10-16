from django.conf.urls import url
from backend.views import *

urlpatterns = [
    url(r'^backend/$', ProductoList.as_view(), name='backend')
]
