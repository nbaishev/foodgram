from django.contrib import admin
from django.contrib.admin import display

from recipes.models import Favourite, Recipe, ShoppingCart


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'added_in_favorites')
    readonly_fields = ('added_in_favorites',)
    list_filter = ('author', 'name', 'tags',)

    @display(description='Количество в избранных')
    def added_in_favorites(self, obj):
        return obj.favorites.count()


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe',)


@admin.register(Favourite)
class FavouriteAdmin(admin.ModelAdmin):
    list_display = ('user', 'recipe',)
