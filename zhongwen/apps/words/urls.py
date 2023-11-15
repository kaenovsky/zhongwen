from django.urls import path

from apps.words.views import WordsTemplateView

urlpatterns = [path("", WordsTemplateView.as_view(), name="words")]