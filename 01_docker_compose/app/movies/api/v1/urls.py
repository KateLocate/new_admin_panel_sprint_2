"""Movies API v1 URLs."""

from django.urls import path

from . import views


urlpatterns = [
    path('movies/<uuid:pk>', views.MoviesDetailApi.as_view()),
    path('movies/', views.MoviesListApi.as_view()),
]
