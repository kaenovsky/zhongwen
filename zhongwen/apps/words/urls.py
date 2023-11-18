from django.urls import path

from apps.words.views import WordsTemplateView, WordTemplateView, WordFormView

urlpatterns = [
    path("", WordsTemplateView.as_view(), name="words"),
    path("<int:id>", WordTemplateView.as_view(), name="word"),
    path("create", WordFormView.as_view(), name="word_create"),
]