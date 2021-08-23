from django.urls import path
import products.views

app_name = 'products'

urlpatterns = [
    path('', products.views.products, name='product')
]
