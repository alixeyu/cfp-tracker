from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from . import models
from . import serializers


class RecipeViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet
):
    queryset = models.Recipe.objects.all()
    serializer_class = serializers.RecipeSerializer
