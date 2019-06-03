from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader

from .forms import NegaposiForm

import MeCab
wakati = MeCab.Tagger("-Owakati")

import os
from django.conf import settings

import fasttext as ft
classifier = ft.load_model(os.path.join(settings.BASE_DIR, 'bin/negaposi.bin'))

# https://docs.djangoproject.com/en/2.2/topics/forms/
def index(request):
    if request.method == 'POST':
        form = NegaposiForm(request.POST)
    else:
        form = NegaposiForm()

    result = ''

    # is_validしないと値を取り出せない
    if form.is_valid():
        content = form.cleaned_data['content'].strip()
        words = wakati.parse(content).strip()
        print(words)
        estimate = classifier.predict([words], k=2)
        estimate_2 = classifier.predict_proba([words], k=2)
        print(estimate[0])
        if estimate[0][0] == "__label__1,":
            print('ネガティブ', estimate_2[0][0][1])
            if estimate_2[0][0][1] > 0.8:
                result = '君、結構ネガティブやなぁ'
            elif estimate_2[0][0][1] > 0.6:
                result = '君、まぁまぁネガティブやなぁ'
            elif estimate_2[0][0][1] > 0.5:
                result = '君はよくわからんな'

        elif estimate[0][0] == "__label__2,":
            print('ポジティブ', estimate_2[0][0][1])
            if estimate_2[0][0][1] > 0.8:
                result = '君、結構ポジティブやなぁ'
            elif estimate_2[0][0][1] > 0.6:
                result = '君、まぁまぁポジティブやなぁ'
            elif estimate_2[0][0][1] > 0.5:
                result = '君はよくわからんな'

    # settings.pyにnegaposi登録していないと読み込めないので注意
    return render(request, 'negaposi/index.html', {'form': form, 'result': result})
