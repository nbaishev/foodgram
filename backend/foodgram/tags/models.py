from django.core.validators import RegexValidator
from django.db import models


class Tag(models.Model):
    """Модель для тегов."""

    name = models.CharField(
        verbose_name='Название тега',
        max_length=100,
        unique=True,
    )
    color = models.CharField(
        verbose_name='Цвет в HEX',
        unique=True,
        max_length=7,
        validators=[
            RegexValidator(
                regex='^#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})$',
                message='Введенное значение не является цветом в формате HEX!'
            )
        ]
    )
    slug = models.SlugField(
        verbose_name='Уникальный слаг',
        max_length=100,
        unique=True,
    )

    class Meta:
        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name
