from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.words.models import Word

# convert querySet to list
words_list = list(Word.objects.all())

class WordsTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "words.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['es'] = words_list[0].es
        context['en'] = words_list[0].en
        context['zw'] = words_list[0].zw
        context['pinyin'] = words_list[0].pinyin
        return context