from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"), 
    path("wiki/<str:name>", views.greet, name="greet"),
    path("search", views.search, name="search"),
    path("randomPage", views.randomPage, name="randomPage"),
    path("create", views.create, name="create"),
    path("edit/<str:name>", views.edit, name="edit"),
    path("submit", views.submit, name="submit"),
    # path("foobar", views.foobar, name="foobar")
]
