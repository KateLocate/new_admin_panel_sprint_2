"""Movies API v1 URLs."""

from django.urls import path, re_path

from . import views


urlpatterns = [
    path('movies/<uuid:pk>', views.MoviesDetailApi.as_view()),
    re_path(r'movies(/)?', views.MoviesListApi.as_view()),
]
