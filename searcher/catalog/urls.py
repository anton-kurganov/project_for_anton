from django.urls import path

from . import views, csvToDjango

app_name = 'catalog'

urlpatterns = [
    path('', views.products, name='products'),
    path('products/<int:id>/', views.products_detail, name='products_detail'),
    path('providers/', views.providers, name='providers'),
    path('providers/<int:id>/', views.providers_detail, name='providers_detail'),
    path('csvtodjango/add_globalfoods/', csvToDjango.add_globalfoods),
    path('csvtodjango/add_arosa/', csvToDjango.add_arosa),
    path('csvtodjango/add_alliance/', csvToDjango.add_alliance),
    path('csvtodjango/add_wilcome/', csvToDjango.add_wilcome),
    path('csvtodjango/add_wilcome/', csvToDjango.add_wilcome),
    path('csvtodjango/delete_all_providers/', csvToDjango.delete_all_providers),
    path('csvtodjango/add_all_providers/', csvToDjango.add_all_providers),
]
