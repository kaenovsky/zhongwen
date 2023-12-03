import os
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.words.models import Word
from apps.words.forms import WordForm

class WordsTemplateView(TemplateView):
    template_name = "words.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["words"] = Word.objects.all()
        return context

class WordTemplateView(TemplateView):
    template_name = "word.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = kwargs.get("id")
        context["word"] = get_object_or_404(Word, id=id) 
        return context

class AddWordTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "word_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = WordForm() 
        return context

    def post(self, request):
        form = WordForm(request.POST)

        if form.is_valid():
            word = form.save(commit=False)
            word.save()
            return redirect("word_success")
        
        return self.render_to_response({"form": form})

class EditWordUpdateView(LoginRequiredMixin, UpdateView):
    model = Word
    form_class = WordForm
    template_name = "word_update.html"

    def get_success_url(self):
        return reverse("word_success")

    def get(self, request, *args, **kwargs):
        word = self.get_object()
        return super().get(request, *args, **kwargs)

class RemoveWordDeleteView(LoginRequiredMixin, DeleteView):
    model = Word
    template_name = "word_delete.html"

    def get_success_url(self):
        return reverse("word_success_del")

    def get(self, request, *args, **kwargs):
        word = self.get_object()
        return super().get(request, *args, **kwargs)

# Templates create/update and word removed

class WordSuccess(LoginRequiredMixin, TemplateView):
    template_name = "word_success.html"

class WordSuccessDel(LoginRequiredMixin, TemplateView):
    template_name = "word_success_del.html"
