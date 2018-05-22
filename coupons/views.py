from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.decorators.http import require_POST
from .models import Coupons
from .forms import CouponsApplyForm

@require_POST
def coupon_apply(request):
    now = timezone.now()
    form = CouponsApplyForm(request.POST)
    if form.is_valid():
        code = form.cleaned_data['code']
        try:
            coupon = Coupons.objects.get(code__iexact=code,
                                    valid_from__lte=now,
                                    valid_to__gte=now,
                                    active=True)
            request.session['coupon_id'] = coupon.id
        except Coupons.DoesNotExist:
            request.session['coupon_id'] = None
    return redirect('cart:cart_detail')