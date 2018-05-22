# -*- coding: utf-8 -*-  
# author: xulang time: 18-3-23
from .cart import Cart


def cart(request):
    return {'cart': Cart(request)}