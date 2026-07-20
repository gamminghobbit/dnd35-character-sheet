from django.urls import path

from . import views


app_name = "characters"

urlpatterns = [
    path("", views.character_builder, name="character_builder"),
]