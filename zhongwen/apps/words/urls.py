from django.urls import path

from apps.words.views import WordsTemplateView, WordTemplateView, WordFormView, WordSuccess #, WordUpdateFormView

urlpatterns = [
    path("", WordsTemplateView.as_view(), name="words"),
    path("<int:id>", WordTemplateView.as_view(), name="word"),
    path("create", WordFormView.as_view(), name="word_create"),
    path("word_success", WordSuccess.as_view(), name="word_success"),
    # path("<int:id>/update", WordUpdateFormView.as_view(), name="word_update"),
]