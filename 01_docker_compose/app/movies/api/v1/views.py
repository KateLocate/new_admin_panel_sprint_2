"""API views for movies app."""

from django.http import JsonResponse

from django.views import View


class MoviesListApi(View):
    """Represents a view class for serializing information about movies."""

    http_method_names = ['get']

    def get(self, request, *args, **kwargs):
        """Main request-response function.

        Parameters:
            request (HttpRequest): Object containing get-request details
            *args (tuple): Any positional arguments
            **kwargs (dict): Any keyword arguments

        Returns:
            JsonResponse: Returns a serialized QuerySet
        """
        return JsonResponse({})
