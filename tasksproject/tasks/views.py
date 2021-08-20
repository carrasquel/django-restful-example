from django.contrib.auth import get_user_model

from rest_framework import authentication, permissions, viewsets

from .models import ToDo
from .serializers import ToDoSerializer, UserSerializer


class DefaultsMixin(object):

    """Default settings for view authentication, permissions,
    filtering and pagination."""

    authentication_classes = (
        authentication.BasicAuthentication,
        authentication.TokenAuthentication,
    )
    
    permission_classes = (
        permissions.IsAuthenticated,
    )
    
    paginate_by = 25
    paginate_by_param = 'page_size'
    max_paginate_by = 100


class ToDoViewSet(DefaultsMixin, viewsets.ModelViewSet):

    queryset = ToDo.objects.order_by('task')
    serializer_class = ToDoSerializer

User = get_user_model()


class UserViewSet(DefaultsMixin, viewsets.ReadOnlyModelViewSet):
    """API endpoint for listing users."""
    
    lookup_field = User.USERNAME_FIELD
    lookup_url_kwarg = User.USERNAME_FIELD
    queryset = User.objects.order_by(User.USERNAME_FIELD)
    serializer_class = UserSerializer

