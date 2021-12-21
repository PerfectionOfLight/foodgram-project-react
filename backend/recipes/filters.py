import django_filters

from .models import Ingredient, Recipe, ReceiptTag


class RecipeFilter(django_filters.FilterSet):
    tags = django_filters.AllValuesMultipleFilter(
        field_name='receipttag__tag__slug',
        method='get_tag'
    )
    is_favorited = django_filters.BooleanFilter(
        method='get_favorite'
    )
    is_in_shopping_cart = django_filters.BooleanFilter(
        method='get_in_shopping_cart'
    )

    class Meta:
        model = Recipe
        fields = (
            'is_favorited',
            'is_in_shopping_cart',
            'author',
            'tags'
        )

    def get_tag(self, queryset, name, value):
        if value:
            return ReceiptTag.objects.filter(
                tags=None
            )
        return ReceiptTag.objects.filter(
            tags=None
        )

    def get_favorite(self, queryset, name, value):
        if value:
            return Recipe.objects.filter(
                favorites__user=self.request.user
            )
        return Recipe.objects.all()

    def get_in_shopping_cart(self, queryset, name, value):
        if value:
            return Recipe.objects.filter(
                shopping_cart__user=self.request.user
            )
        return Recipe.objects.all()


class IngredientFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(
        field_name='name',
        lookup_expr='icontains'
    )

    class Meta:
        model = Ingredient
        fields = ('name',)
