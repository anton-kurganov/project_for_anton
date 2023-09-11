import csv, os
from .models import Product, Provider
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
prov_gf = get_object_or_404(Provider, id=1)
prov_wilcome = get_object_or_404(Provider, id=2)
prov_alliance = get_object_or_404(Provider, id=3)
prov_arosa = get_object_or_404(Provider, id=4)

def test_create(request):
    Product.objects.create(
        title='Писюн',
        provider=prov_gf,
        price_for_unit=1000,
        unit_type='Кол-во'
    )
    return redirect(reverse('catalog:products'))


def add_globalfoods(request):
    c = '0123456789'
    products = Product.objects.filter(provider=prov_gf)
    products.delete()
    with open("catalog/csv/globalfoods.csv", 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if row[0] != '':
                if row[0][0] in c:
                    Product.objects.create(
                        title=row[2],
                        provider=prov_gf,
                        price_for_unit=row[5],
                        unit_type=row[4],
                        code=row[1],
                        in_box=row[3]
                    )
    return redirect(reverse('catalog:products'))


def add_arosa(request):
    products = Product.objects.filter(provider=prov_arosa)
    products.delete()
    with open("catalog/csv/arosa.csv", 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if row[0] != '' and len(row[0]) == 11:
                Product.objects.create(
                    code=row[0],
                    title=row[1],
                    provider=prov_arosa,
                    country=row[3],
                    price_for_unit=row[4],
                    in_box=row[6],
                    unit_type=row[7]
                )
    return redirect(reverse('catalog:products'))


def add_alliance(request):
    products = Product.objects.filter(provider=prov_alliance)
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
                        provider=prov_alliance,
                        country=row[3],
                        price_for_unit=row[7],
                        in_box=row[6],
                        unit_type=row[4]
                    )
    return redirect(reverse('catalog:products'))


def add_wilcome(request):
    products = Product.objects.filter(provider=prov_wilcome)
    products.delete()

    with open("catalog/csv/wilcome.csv", 'r') as file:
        reader = csv.reader(file, delimiter=';')
        for row in reader:
            if row[1] != '':
                Product.objects.create(
                    title=row[0],
                    provider=prov_wilcome,
                    price_for_unit=row[2],
                    unit_type=row[1]
                )
    return redirect(reverse('catalog:products'))
                


    
                    
