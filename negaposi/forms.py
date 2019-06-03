from django.db import models

# Create your models here.


from django import forms

class NegaposiForm(forms.Form):
    content = forms.CharField(
        label='判定したい文章（5000文字以内）',
        max_length=5000,
        required=False,
        help_text='文章をかいてください',
        widget=forms.Textarea
    )
