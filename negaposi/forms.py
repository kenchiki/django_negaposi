from django.db import models

# Create your models here.


from django import forms

class NegaposiForm(forms.Form):
    content = forms.CharField(
        label='文章',
        max_length=5000,
        required=False,
        help_text='文章をかいてください',
        widget=forms.Textarea
    )
