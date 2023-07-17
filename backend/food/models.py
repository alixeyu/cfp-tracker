from django.db import models


class Recipe(models.Model):
    image = models.ImageField()
    title = models.CharField(max_length=100)
    description = models.TextField(default='')
    ingredients = models.ManyToManyField('Ingredient')

    def __str__(self) -> str:
        return f'{self.__class__.__name__} "{self.title}"'


class Ingredient(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(default='')

    def __str__(self) -> str:
        return f'{self.__class__.__name__} "{self.title}"'
