import os
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.words.models import Word
from apps.words.forms import WordForm

class WordsTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "words.html"

    def get_context_data(self, **kwargs):
        first_word = Word.objects.get(id=1)
        context = super().get_context_data(**kwargs)
        context['first_word'] = first_word        
        return context

class WordTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "word.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        word = Word.objects.get(id=kwargs['id'])
        if not word:
            pass
        context["word"] = word 
        return context
    
class WordFormView(LoginRequiredMixin, CreateView):
    form_class = WordForm
    template_name = 'word_create.html'
    success_url = reverse_lazy('word_success')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

class WordSuccess(LoginRequiredMixin, TemplateView):
    template_name = "word_success.html"

# class WordUpdateFormView(LoginRequiredMixin, CreateView):
#     form_class = WordForm
#     template_name = 'word_update.html'
#     success_url = reverse_lazy('words')

#     def form_valid(self, form):
#         form.save()
#         return super().form_valid(form)