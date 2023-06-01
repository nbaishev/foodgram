import json

from django.core.management.base import BaseCommand

from ingredients.models import Ingredient

class Command(BaseCommand):

    help = 'Импорт ингредиентов'

    def handle(self, *args, **options):
        with open('ingredients.json', 'r') as file:
            data = json.load(file)

        for note in data:
            try:
                Ingredient.objects.get_or_create(**note)
                print(f"{note['name']} в базе")
            except Exception as error:
                print(f'Ошибка при добавлении {error}')

        print('Загрузка ингредиентов завершена')
