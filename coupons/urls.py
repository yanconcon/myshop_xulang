# -*- coding: utf-8 -*-  
# author: xulang time: 18-5-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^apply/$', views.coupon_apply, name='apply'),
]