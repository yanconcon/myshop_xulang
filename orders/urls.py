# -*- coding: utf-8 -*-  
# author: xulang time: 18-3-23
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
]