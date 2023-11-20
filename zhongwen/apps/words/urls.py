from django.urls import path

from apps.words.views import (
    WordsTemplateView,
    WordTemplateView,
    AddWordTemplateView,
    EditWordUpdateView,
    RemoveWordDeleteView,
    WordSuccess,
    WordSuccessDel,
)

urlpatterns = [
    path("", WordsTemplateView.as_view(), name="words"),
    path("<int:id>", WordTemplateView.as_view(), name="word"),
    path("create", AddWordTemplateView.as_view(), name="word_create"),
    path("<int:pk>/update", EditWordUpdateView.as_view(), name="word_update"),
    path("<int:pk>/delete", RemoveWordDeleteView.as_view(), name="word_delete"),
    path("word_success", WordSuccess.as_view(), name="word_success"),
    path("word_success_del", WordSuccessDel.as_view(), name="word_success_del"),
]