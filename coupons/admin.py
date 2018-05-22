from django.contrib import admin
from .models import Coupons
# Register your models here.


class CounponsAdmin(admin.ModelAdmin):
    list_display = ['code', 'valid_from', 'valid_to', 'discount', 'active']
    list_filter = ['active', 'valid_from', 'valid_to']
    search_fields = ['code']

admin.site.register(Coupons, CounponsAdmin)