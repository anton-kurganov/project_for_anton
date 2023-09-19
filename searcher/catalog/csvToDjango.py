import csv
from .models import Product, Provider
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse

providers = {
    'globalfoods': get_object_or_404(Provider, id=1),
    'wilcome': get_object_or_404(Provider, id=2),
    'alliance': get_object_or_404(Provider, id=3),
    'arosa': get_object_or_404(Provider, id=4),
    'proekt': get_object_or_404(Provider, id=5),
    'marussia': get_object_or_404(Provider, id=6),
    'fatucci': get_object_or_404(Provider, id=7),
    'sapori': get_object_or_404(Provider, id=8),
    'metro': get_object_or_404(Provider, id=9),
}


def add_globalfoods(request):
    c = '0123456789'
    products = Product.objects.filter(provider=providers['globalfoods'])
    products.delete()
    with open("catalog/csv/globalfoods.csv", 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if row[0] != '':
                if row[0][0] in c:
                    Product.objects.create(
                        title=row[2],
                        search_field=row[2].lower(),
                        provider=providers['globalfoods'],
                        price_for_unit=number_valid(row[5]),
                        unit_type=row[4],
                        code=row[1],
                        in_box=row[3]
                    )
    return redirect(reverse('catalog:products'))


def add_arosa(request):
    products = Product.objects.filter(provider=providers['arosa'])
    products.delete()
    with open("catalog/csv/arosa.csv", 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if row[0] != '' and len(row[0]) == 11:
                Product.objects.create(
                    code=row[0],
                    title=row[1],
                    search_field=row[1].lower(),
                    provider=providers['arosa'],
                    country=row[3],
                    price_for_unit=number_valid(row[4]),
                    in_box=row[6],
                    unit_type=row[7]
                )
    return redirect(reverse('catalog:products'))


def add_alliance(request):
    products = Product.objects.filter(provider=providers['alliance'])
    products.delete()
    c = '0123456789'
    with open("catalog/csv/alliance.csv", 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if row[1] != '':
                if row[1][0] in c:
                    Product.objects.create(
                        code=row[1],
                        title=row[2][8:],
                        search_field=row[2][8:].lower(),
                        provider=providers['alliance'],
                        country=row[3],
                        price_for_unit=number_valid(row[7]),
                        in_box=row[6],
                        unit_type=row[4]
                    )
    return redirect(reverse('catalog:products'))


def add_wilcome(request):
    products = Product.objects.filter(provider=providers['wilcome'])
    products.delete()

    with open("catalog/csv/wilcome.csv", 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if row[1] != '':
                Product.objects.create(
                    title=row[0],
                    search_field=row[0].lower(),
                    provider=providers['wilcome'],
                    price_for_unit=number_valid(row[2]),
                    unit_type=row[1]
                )
    return redirect(reverse('catalog:products'))


def add_proekt(request):
    products = Product.objects.filter(provider=providers['proekt'])
    products.delete()

    with open("catalog/csv/proekt.csv", 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if row[1] != '' and row[2] != '':
                row[0] = ''.join(row[0].split('\t'))
                Product.objects.create(
                    title=row[0],
                    search_field=row[0].lower(),
                    provider=providers['proekt'],
                    price_for_unit=number_valid(row[1]),
                    unit_type=row[2],
                    in_box=row[3],
                    country=row[4]
                )


def add_metro(request):
    products = Product.objects.filter(provider=providers['metro'])
    products.delete()

    categories = [
        'Poultry', 'Sweets', 'Deep Frozen', 'Soft Drinks', 'Canned Food',
        'Fruits _ Vegetables', 'Dairy', 'Grocery', 'Processed Meat',
        'Fish', 'Bakery', 'Fresh Meat'
    ]
    with open("catalog/csv/metro.csv", 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if row[1] in categories:
                Product.objects.create(
                    title=row[3],
                    search_field=row[3].lower(),
                    provider=providers['metro'],
                    price_for_unit=number_valid(row[6]),
                    unit_type=row[4] + " шт",
                    code=row[2]
                )


def add_marussia(request):
    products = Product.objects.filter(provider=providers['marussia'])
    products.delete()

    with open("catalog/csv/marussia.csv", 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if row[1] != '' and row[3] != '' and row[3] != '-':
                Product.objects.create(
                    title=row[0],
                    search_field=row[0].lower(),
                    provider=providers['marussia'],
                    price_for_unit=number_valid(row[3]),
                    unit_type=row[1]
                )


def add_sapori(request):
    products = Product.objects.filter(provider=providers['sapori'])
    products.delete()

    with open("catalog/csv/sapori.csv", 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            row = row[3:]
            if row[1] != '':
                Product.objects.create(
                    title=row[0],
                    search_field=row[0].lower(),
                    provider=providers['sapori'],
                    price_for_unit=number_valid(row[1]),
                    unit_type="-"
                )


def add_fatucci(request):
    products = Product.objects.filter(provider=providers['fatucci'])
    products.delete()

    with open("catalog/csv/fatucci.csv", 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if row[2] != '':
                Product.objects.create(
                    title=row[0],
                    search_field=row[0].lower(),
                    provider=providers['fatucci'],
                    price_for_unit=number_valid(row[2]),
                    unit_type=row[1]
                )


def delete_all_providers(request):
    for i in providers:
        products = Product.objects.filter(provider=providers[i])
        products.delete()
    return redirect(reverse('catalog:products'))


def number_valid(number):
    if ' ' in number:
        number = ''.join(number.split())
    if ',' in number:
        number = '.'.join(number.split(','))
    if '\xa0' in number:
        number = ''.join(number.split('\xa0'))
    return float(number)


def add_all_providers(request):
    add_alliance('')
    add_arosa('')
    add_globalfoods('')
    add_wilcome('')
    add_proekt('')
    add_fatucci('')
    add_sapori('')
    add_marussia('')
    add_metro('')
    return redirect(reverse('catalog:products'))
