"""API views for movies app."""
from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.detail import BaseDetailView
from django.views.generic.list import BaseListView

from ...models import Filmwork


class MoviesApiMixin:
    model = Filmwork
    http_method_names = ['get']

    def get_queryset(self):
        """Method for getting Filmwork objects and preparing it"""
        movies_objects = self.model.objects.prefetch_related(
            'genres', 'personfilmwork',
        ).values(
            'id', 'title', 'description', 'creation_date', 'rating', 'type',
        )
        movies_with_aggregated_fields = movies_objects.annotate(
            genres=ArrayAgg('genres__name', distinct=True),
            actors=ArrayAgg(
                'personfilmwork__person__full_name', distinct=True, filter=Q(personfilmwork__role='actor'),
            ),
            writers=ArrayAgg(
                'personfilmwork__person__full_name', distinct=True, filter=Q(personfilmwork__role='writer'),
            ),
            directors=ArrayAgg(
                'personfilmwork__person__full_name', distinct=True, filter=Q(personfilmwork__role='director'),
            ),
        )
        return movies_with_aggregated_fields

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(context)


class MoviesListApi(MoviesApiMixin, BaseListView):
    """Represents a view class for serializing information about movies."""

    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        """Method returning dictionary with movies data"""
        movies = self.get_queryset()
        paginator, pg, objs, is_paginated = self.paginate_queryset(movies, self.paginate_by)
        # print(self.request.GET.values())

        page = pg

        page_number = self.request.GET.get('page', None)
        if page_number:
            if page_number.isdigit():
                page = paginator.get_page(page_number)
            elif page_number == 'last':
                page = paginator.get_page(paginator.num_pages)

        context = {
            'count': paginator.count,
            'total_pages': paginator.num_pages,
            'prev': page.previous_page_number() if page.has_previous() else None,
            'next': page.next_page_number() if page.has_next() else None,
            'results': list(page.object_list),
        }
        return context


class MoviesDetailApi(MoviesApiMixin, BaseDetailView):
    """Represents a view class for serializing information about a movie."""

    def get_context_data(self, *, object_list=None, **kwargs):
        """Method returning dictionary with movie data"""
        movie = self.get_queryset()
        context = movie.first()
        return context
