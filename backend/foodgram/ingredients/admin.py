from django.contrib import admin

from ingredients.models import Ingredient, IngredientAmount


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'measurement_unit',)
    list_filter = ('name',)


@admin.register(IngredientAmount)
class IngredientInRecipe(admin.ModelAdmin):
    list_display = ('recipe', 'ingredient', 'amount',)
