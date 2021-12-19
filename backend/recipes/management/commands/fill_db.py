import csv

from django.core.management.base import BaseCommand

from recipes.models import Ingredient


class Command(BaseCommand):
    help = 'Fill the database from .csv files'

    def handle(self, *args, **kwargs):
        try:
            with open(
                'recipes/data/ingredients.csv', encoding='utf-8'
            ) as csvfile:
                if csvfile:
                    reader = csv.reader(csvfile)
                    for row in reader:
                        name, measurement_unit = row
                        Ingredient.objects.get_or_create(
                            name=name, measurement_unit=measurement_unit
                        )
                    self.stdout.write(
                        self.style.SUCCESS(
                            'The ingredients are uploaded to the database.'
                        )
                    )
        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR('The file ingredients.csv not found.')
            )
