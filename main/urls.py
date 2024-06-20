from django.urls import path
from . import views

urlpatterns = [
    path("", views.article_index, name="article_index"),
    path("article/<int:pk>/", views.article_show, name="article_show"),
    path("article/new/", views.article_new, name="article_new"),
]
