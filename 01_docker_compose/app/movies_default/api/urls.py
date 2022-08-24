from django.urls import path, include


urlpatterns = [
    path('v1/', include('movies_default.api.v1.urls')),
]
