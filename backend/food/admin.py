from django.contrib import admin

from . import models


@admin.register(models.Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(models.Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('title', )
