from catalog.models import Provider
from django.shortcuts import get_object_or_404


providers = {
    'horeca': get_object_or_404(Provider, brand='HoReCa'),
    'prod-zakaz': get_object_or_404(Provider, brand='prod-zakaz'),
    'target-market': get_object_or_404(Provider, brand='target-market'),
    # 'unknown': get_object_or_404(Provider, brand=''),
    'global-trade': get_object_or_404(Provider, brand='global-trade'),
    # 'marussia': get_object_or_404(Provider, id=6),
    # 'fatucci': get_object_or_404(Provider, id=7),
    # 'sapori': get_object_or_404(Provider, id=8),
    # 'metro': get_object_or_404(Provider, id=9),
}


def number_valid(number):
    if ' ' in number:
        number = ''.join(number.split())
    if ',' in number:
        number = '.'.join(number.split(','))
    if '\xa0' in number:
        number = ''.join(number.split('\xa0'))
    return float(number)
