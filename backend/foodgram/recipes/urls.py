from django.urls import include, path
from rest_framework.routers import DefaultRouter

from recipes.views import RecipeViewSet

app_name = 'recipes'


router = DefaultRouter()
router.register('recipes', RecipeViewSet, basename='recipes')

urlpatterns = [
    path('', include(router.urls))
]
