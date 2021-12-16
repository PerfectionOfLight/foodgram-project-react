import csv

from django.core.management.base import BaseCommand
from recipes.models import Ingredients


class Command(BaseCommand):
    help = 'Fill the database from .csv files'

    def handle(self, *args, **kwargs):
        try:
            with open(
                'static/data/users.csv', encoding='utf-8'
            ) as csvfile:
                if csvfile:
                    reader = csv.DictReader(csvfile)
                    for row in reader:
                        Ingredients.objects.get_or_create(
                            name=row['name'],
                            measurement_unit=row['measurement_unit']
                            )
                    self.stdout.write(
                        self.style.SUCCESS(
                            'The users are uploaded to the database.'
                        )
                    )
        except FileNotFoundError:
            self.stdout.write(
                self.style.ERROR('The file users.csv not found.')
            )
