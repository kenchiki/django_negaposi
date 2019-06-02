from django.db import models

# Create your models here.

# https://narito.ninja/blog/detail/98/参考

from django import forms

class NegaposiForm(forms.Form):
    content = forms.CharField(
        label='文章', max_length=500,
        required=False, help_text='文章をかいてください'
    )
