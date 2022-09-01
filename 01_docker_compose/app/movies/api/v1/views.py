"""API views for movies app."""
from django.contrib.postgres.aggregates import ArrayAgg
from django.db.models import Q
from django.http import JsonResponse
from django.views.generic.list import BaseListView

from ...models import Filmwork


class MoviesListApi(BaseListView):
    """Represents a view class for serializing information about movies."""

    model = Filmwork
    http_method_names = ['get']

    @staticmethod
    def agg_movies_query(movies_query):
        """Static method with aggregating logic for the Filmwork model"""
        query_with_vals = movies_query.prefetch_related(
            'genres', 'personfilmwork',
        ).values(
            'id', 'title', 'description', 'creation_date', 'rating', 'type',
        )
        query_with_aggregated_fields = query_with_vals.annotate(
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
        return query_with_aggregated_fields

    def get_queryset(self):
        """Method for getting database objects and preparing it"""
        movies = self.model.objects.all()
        movies_with_aggregated_fields = self.agg_movies_query(movies)
        return movies_with_aggregated_fields

    def get_context_data(self, *, object_list=None, **kwargs):
        """Method returning dictionary with movies data"""
        context = {
            'results': list(self.get_queryset()),
        }
        return context

    def render_to_response(self, context, **response_kwargs):
        """Method formatting the response. Returns a response with data from the given context."""
        return JsonResponse(context)


class SingleMovieApi(MoviesListApi):
    """Represents a view class for serializing information about a movie."""

    def get_queryset(self):
        """Method for getting database objects and preparing it"""
        movie = self.model.objects.filter(id=self.kwargs['uuid'])
        movie_with_aggregated_fields = self.agg_movies_query(movie)
        return movie_with_aggregated_fields
