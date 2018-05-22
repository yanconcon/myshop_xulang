from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    # 显示所有商品及其种类，不接收参数
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    # 接收参数category_slug,当点击某一个种类时，就只显示这个种类的商品,
    # 这里的category_slug是指url(r'^(?P<category_slug>[-\w]+)/$', views.product_list, )里的<category_slug>
    if category_slug:
        # 获取与slug对应的种类
        category = get_object_or_404(Category, slug=category_slug)
        # 获取与该种类对应的商品们
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html', {'category': category,
                                                      'categories': categories,
                                                      'products': products})


# 接收id 和slug作为参数来检索Product实例
def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request,
                  'shop/product/detail.html',
                  {'product': product,
                   'cart_product_form': cart_product_form})
