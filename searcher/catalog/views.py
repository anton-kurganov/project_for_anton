from django.shortcuts import render, get_object_or_404
from .models import Product, Provider


def products(request):
    search_query = request.GET.get('search', '')

    if search_query:
        if len(search_query) > 4:
            search_query = search_query[1:-1]
        product_list = (Product
                        .objects
                        .select_related('provider')
                        .filter(search_field__icontains=search_query)
                        .order_by('-price_for_unit')
                        )
    else:
        product_list = (Product
                        .objects
                        .select_related('provider')
                        .order_by('-price_for_unit')
                        .all())
    context = {
        'product_list': product_list,
    }
    return render(request, 'catalog/products.html', context)


def products_detail(request, id):
    product = get_object_or_404(Product, id=id)
    context = {
        'product': product
    }
    return render(request, 'catalog/products_detail.html', context)


def providers(request):
    provider_list = Provider.objects.all()
    context = {
        'provider_list': provider_list
    }
    return render(request, 'catalog/providers.html', context)


def providers_detail(request, id):
    provider = get_object_or_404(Provider, id=id)
    product_list = Product.objects.filter(provider=provider)
    context = {
        'provider': provider,
        'product_list': product_list,
    }
    return render(request, 'catalog/providers_detail.html', context)
