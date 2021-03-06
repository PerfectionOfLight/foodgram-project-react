from django.contrib import admin

from .models import Favorite, Ingredient, Recipe, ShoppingCart, Tag
from .forms import AtLeastOneFormSet


class RecipeTagInline(admin.TabularInline):
    model = Recipe.tags.through
    extra = 1
    formset = AtLeastOneFormSet


class RecipeIngredientInline(admin.TabularInline):
    model = Recipe.ingredients.through
    extra = 1
    formset = AtLeastOneFormSet


@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    fields = ('author',
              'name',
              'image',
              'text',
              'cooking_time',
              )
    readonly_fields = (
        'pub_date',
    )
    list_filter = (
        'author',
        'name',
    )
    empty_value_display = '-пусто-'
    inlines = (RecipeTagInline, RecipeIngredientInline)


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'measurement_unit'
    )
    list_filter = (
        'name',
    )
    empty_value_display = '-пусто-'


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fields = (
        'name',
        'color',
        'slug'
    )
    empty_value_display = '-пусто-'


@admin.register(Favorite)
class FavoriteAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'recipe',
        'added_date'
    )


@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'recipe',
        'added_date'
    )
