import os
from django.shortcuts import get_object_or_404, render, redirect
from django.urls import reverse
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from apps.numbs.models import Numb
from apps.numbs.forms import NumbForm

class NumbsTemplateView(TemplateView):
    template_name = "numbers.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["numbs"] = Numb.objects.all()
        return context

class NumbTemplateView(TemplateView):
    template_name = "number.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = kwargs.get("id")
        context["number"] = get_object_or_404(Numb, id=id) 
        return context

class AddNumbTemplateView(LoginRequiredMixin, TemplateView):
    template_name = "number_create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = NumbForm() 
        return context

    def post(self, request):
        form = NumbForm(request.POST)

        if form.is_valid():
            number = form.save(commit=False)
            number.save()
            return redirect("number_success")
        
        return self.render_to_response({"form": form})

class EditNumbUpdateView(LoginRequiredMixin, UpdateView):
    model = Numb
    form_class = NumbForm
    template_name = "number_update.html"

    def get_success_url(self):
        return reverse("number_success")

    def get(self, request, *args, **kwargs):
        number = self.get_object()
        return super().get(request, *args, **kwargs)

class RemoveNumbDeleteView(LoginRequiredMixin, DeleteView):
    model = Numb
    template_name = "number_delete.html"

    def get_success_url(self):
        return reverse("number_success_del")

    def get(self, request, *args, **kwargs):
        number = self.get_object()
        return super().get(request, *args, **kwargs)

# Templates create/update and number removed

class NumbSuccess(LoginRequiredMixin, TemplateView):
    template_name = "number_success.html"

class NumbSuccessDel(LoginRequiredMixin, TemplateView):
    template_name = "number_success_del.html"
