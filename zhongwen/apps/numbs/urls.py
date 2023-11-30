from django.urls import path

from apps.numbs.views import (
    NumbsTemplateView,
    NumbTemplateView,
    AddNumbTemplateView,
    EditNumbUpdateView,
    RemoveNumbDeleteView,
    NumbSuccess,
    NumbSuccessDel,
)

urlpatterns = [
    path("", NumbsTemplateView.as_view(), name="numbers"),
    path("<int:id>", NumbTemplateView.as_view(), name="number"),
    path("create", AddNumbTemplateView.as_view(), name="number_create"),
    path("<int:pk>/update", EditNumbUpdateView.as_view(), name="number_update"),
    path("<int:pk>/delete", RemoveNumbDeleteView.as_view(), name="number_delete"),
    path("number_success", NumbSuccess.as_view(), name="number_success"),
    path("number_success_del", NumbSuccessDel.as_view(), name="number_success_del"),
]