from django.urls import path
import baskets.views
app_name = 'baskets'

urlpatterns = [
    path('add/<int:product_id>', baskets.views.basket_add, name='basket_add'),
    path('remove/<int:basket_id>', baskets.views.basket_remove, name='basket_remove'),
    path('edit/<int:id>/<int:quantity>/', baskets.views.basket_edit, name='basket_edit'),
]
