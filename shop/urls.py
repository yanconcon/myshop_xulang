# -*- coding: utf-8 -*-  
# author: xulang time: 18-3-20
from django.conf.urls import url
from . import views


urlpatterns = [
    # 不带参数调用product_list()视图，显示所有商品及其种类
    url(r'^$', views.product_list, name='product_list'),
    # 传递一个category_slug参数来调用product_list()视图，这个参数需要我们在模型中定义一个获取绝对URL的动作
    url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]