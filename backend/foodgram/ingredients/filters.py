from django_filters.rest_framework import FilterSet, filters

from ingredients.models import Ingredient


class IngredientFilter(FilterSet):
    """Фильтр ингредиентов по названию."""

    name = filters.CharFilter(lookup_expr='istartswith')

    class Meta:
        model = Ingredient
        fields = ['name']
