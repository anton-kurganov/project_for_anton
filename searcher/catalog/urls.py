from django.urls import path

from . import views

app_name = 'catalog'

urlpatterns = [
    path('', views.products, name='products'),
    path('products/<int:id>/', views.products_detail, name='products_detail'),
    path('providers/', views.providers, name='providers'),
    path('providers/<int:id>/', views.providers_detail,
         name='providers_detail'),
]
