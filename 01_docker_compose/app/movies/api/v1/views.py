"""API views for movies app."""
from django.contrib.postgres.aggregates import ArrayAgg

from django.db.models import Count, Q

from django.http import JsonResponse
from django.views import View
from django.views.generic.list import BaseListView

from ...models import Filmwork


class MoviesListApi(BaseListView):
    #  Fields needed:
    #   id, title, description, creation_date, rating, type,
    #   genre_name (list),
    #   actors (list of names), directors (list of names), writers (list of names),

    """Represents a view class for serializing information about movies."""

    model = Filmwork
    http_method_names = ['get']

    def get_queryset(self):
        """Method of getting database objects and preparing it"""
        movies_query = self.model.objects.prefetch_related('genres', 'personfilmwork')
        movies = movies_query.values('id', 'title', 'description', 'creation_date', 'rating', 'type')
        movies_with_aggregated_fields = movies.annotate(
            genres=ArrayAgg('genres__name', distinct=True),
        ).annotate(
            actors=ArrayAgg('personfilmwork__person__full_name', distinct=True, filter=Q(personfilmwork__role='actor')),
            writers=ArrayAgg('personfilmwork__person__full_name', distinct=True, filter=Q(personfilmwork__role='writer')),
            directors=ArrayAgg('personfilmwork__person__full_name', distinct=True, filter=Q(personfilmwork__role='director')),
        )
        print(movies_with_aggregated_fields.query)
        cnt = movies.aggregate(
            cnt=Count('id')
        )

        return movies_with_aggregated_fields

    def get_context_data(self, *, object_list=None, **kwargs):
        """Method returning dictionary with movies data

        Parameters:
            object_list
            **kwargs (dict): Any keyword arguments

        Returns:
            context (dict): Returns a serialized QuerySet
        """

        context = {
            'results': list(self.get_queryset()),
        }
        return context

    def render_to_response(self, context, **response_kwargs):
        """Method formatting the response. Returns a response with a
        structure from the given context.

        Pass response_kwargs to the constructor of the response class.
        Parameters:
            context
            **response_kwargs (dict): Any keyword arguments

        Returns:
            JsonResponse: Returns a serialized QuerySet
        """
        return JsonResponse(context)


class SingleMovieApi(View):
    """Represents a view class for serializing information about a movie."""

    model = Filmwork
    http_method_names = ['get']

    def get_queryset(self, uuid):
        """Method of getting database objects and preparing it"""
        object = self.model.objects.get(id=uuid)
        return object

    def get_context_data(self, *, object_list=None, **kwargs):
        """Method returning dictionary with movies data

        Parameters:
            object_list
            **kwargs (dict): Any keyword arguments

        Returns:
            context (dict): Returns a serialized QuerySet
        """

        context = {
            'results': list(self.get_queryset()),
        }
        return context

    def render_to_response(self, context, **response_kwargs):
        """Method formatting the response. Returns a response with a
        structure from the given context.

        Pass response_kwargs to the constructor of the response class.
        Parameters:
            context
            **response_kwargs (dict): Any keyword arguments

        Returns:
            JsonResponse: Returns a serialized QuerySet
        """
        return JsonResponse(context)
