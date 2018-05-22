# -*- coding: utf-8 -*-  
# author: xulang time: 18-5-8
from django import forms


class CouponsApplyForm(forms.Form):
    code = forms.CharField()