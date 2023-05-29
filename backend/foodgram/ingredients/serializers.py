from rest_framework import serializers
from rest_framework.fields import IntegerField

from ingredients.models import IngredientAmount, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    """Сериализатор для модели Ingredient."""

    class Meta:
        fields = '__all__'
        model = Ingredient


class IngredientAmountSerializer(serializers.ModelSerializer):
    """Сериализатор для модели IngredientAmount."""

    id = IntegerField(write_only=True)

    class Meta:
        model = IngredientAmount
        fields = ('id', 'amount')
