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
                        price_for_unit=row[5],
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
                    price_for_unit=row[4],
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
                        price_for_unit=row[7],
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
                    price_for_unit=row[2],
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
                    price_for_unit=row[1],
                    unit_type=row[2],
                    in_box=row[3],
                    country=row[4]
                )


def delete_all_providers(request):
    for i in providers:
        products = Product.objects.filter(provider=providers[i])
        products.delete()
    return redirect(reverse('catalog:products'))


def add_all_providers(request):
    add_alliance('')
    add_arosa('')
    add_globalfoods('')
    add_wilcome('')
    add_proekt('')
    return redirect(reverse('catalog:products'))
