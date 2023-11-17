from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class WordsTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "words.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context