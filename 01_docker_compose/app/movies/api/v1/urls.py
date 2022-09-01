"""Movies API v1 URLs."""

from django.urls import path

from . import views


urlpatterns = [
    path('movies/', views.MoviesListApi.as_view()),
    path('movies/<uuid:uuid>/', views.SingleMovieApi.as_view()),
]
