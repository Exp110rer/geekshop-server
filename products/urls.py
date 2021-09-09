from django.urls import path
import products.views

app_name = 'products'

urlpatterns = [
    path('', products.views.products, name='product'),
    path('<int:category_id>', products.views.products, name='category'),
    path('page/<int:page>', products.views.products, name='page'),
]
