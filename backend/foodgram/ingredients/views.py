from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from ingredients.filters import IngredientFilter
from ingredients.models import Ingredient
from ingredients.serializers import IngredientSerializer
from utils.permissions import IsAdminOrReadOnly


class IngredientViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer
    permission_classes = (IsAdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = IngredientFilter
