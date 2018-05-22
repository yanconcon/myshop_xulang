from django.db import models
from django.core.urlresolvers import reverse


# 产品类型
class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        # 用slug来生成名为product_list_by_category的url里的<category_slug>
        return reverse('shop:product_list_by_category', args=[self.slug])


# 产品
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products')
    name = models.CharField(max_length=200, db_index=True)
    # 用来建立产品URL的slug
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)  # ?
    description = models.TextField(blank=True)
    # 十进制字段，使用该字段可避免精度问题，后面分别是数字最大值，小数位数,
    price = models.DecimalField(max_digits=10, decimal_places=2)
    # 正整数字段，用来保存产品库存
    stock = models.PositiveIntegerField()
    # 展示产品是否可供购买的布尔值
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)
        # 指定index和id共同提供引索
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail', args=[self.id, self.slug])
