import csv

from django.core.management.base import BaseCommand
from catalog.models import Product
from core.csv_core import providers, number_valid


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        Product.objects.all().delete()
        self.horeca()
        self.prod_zakaz()
        self.target_market()
        # self.unknown()
        self.global_trade()
        return "Import was completed successfully!"

    def horeca(self):
        with open("catalog/csv/horeca.csv", 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if len(row[3]) > 3:
                    Product.objects.create(
                        code=row[3],
                        title=row[7],
                        search_field=row[7].lower(),
                        provider=providers['horeca'],
                        price_for_unit=number_valid(row[46]),
                        in_box=row[40],
                        unit_type=row[43]
                    )

    def prod_zakaz(self):
        with open("catalog/csv/prod-zakaz.csv", 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if row[2] != 'ждём' and row[2] != '':
                    Product.objects.create(
                        title=row[0],
                        search_field=row[0].lower(),
                        provider=providers['prod-zakaz'],
                        price_for_unit=number_valid(row[2]),
                        unit_type=row[1]
                    )

    def target_market(self):
        with open("catalog/csv/target-market.csv", 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if row[1] != '':
                    Product.objects.create(
                        title=row[0],
                        search_field=row[0].lower(),
                        provider=providers['target-market'],
                        price_for_unit=number_valid(row[1]),
                    )

    def unknown(self):
        with open("catalog/csv/unkown.csv", 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                Product.objects.create(
                    title=row[1],
                    search_field=row[1].lower(),
                    provider=providers['unkown'],
                    price_for_unit=number_valid(row[3]),
                    unit_type=row[2]
                )

    def global_trade(self):
        with open("catalog/csv/global-trade.csv", 'r') as file:
            reader = csv.reader(file, delimiter=';')
            for row in reader:
                if row[1] != 'под заказ' and row[1] != '' and row[1] != '*':
                    Product.objects.create(
                        title=row[0],
                        price_for_unit=number_valid(row[1][:-2]),
                        provider=providers['global-trade'],
                    )
