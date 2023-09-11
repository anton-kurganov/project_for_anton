from django.contrib import admin

from .models import Product, Provider

admin.site.register(Provider)
admin.site.register(Product)
