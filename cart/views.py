from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from shop.models import Product
from .cart import Cart
from .forms import CartAddProductForm
from coupons.forms import CouponsApplyForm


@require_POST
# 该方法仅在商品详情页面product_detail使用。
# 这里的参数product_id指的是product_detail模板里添加的参数product.id
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 # 如果在商品详情页面，这里form表单里的update的值一直会是False.那么add()索添加的数量就永远只会在原来的基础上增加
                 # 比如第一次在某商品详情页面添加了2件进入购物车，再返回来再添加4件，那么总数会变成6件而不是重新变成4件
                 # 如果在购物车页面，重新修改某件商品数量，我们在会将update值定为True，再次调用cart_add方法，数量就会重新按照给定的值更新
                 update_quantity=cd['update'])
    # 重新定向到cart_detail视图，让购物车详情模板展示cart里面的东西
    return redirect('cart:cart_detail')


def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:cart_detail')


def cart_detail(request):
    cart = Cart(request)
    for item in cart:
        # 为了让用户能在购物车里改变每件产品的数量，而为每个商品创建了一个CartAddProductForm实例
        item['update_quantity_form'] = CartAddProductForm(
            # 把表单和当前数量在重新初始化，将form表单里的update值修改为True
            initial={'quantity': item['quantity'],
                     'update': True})
    coupon_apply_form = CouponsApplyForm()
    return render(request, 'cart/detail.html', {'cart': cart, 'coupon_apply_form': coupon_apply_form})
