from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    CartView,
    IncreaseQuantityView,
    DecreaseQuantityView,
    DeleteItemView,
    CheckoutView,
)

app_name = 'cart'
urlpatterns = (
    path('', CartView.as_view(), name='summary'),
    path('shop/', ProductListView.as_view(), name='product_list'),
    path('shop/<slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('increase-quantity/<pk>/', IncreaseQuantityView.as_view(), name='increase_quantity'),
    path('decrease-quantity/<pk>/', DecreaseQuantityView.as_view(), name='decrease_quantity'),
    path('delete-item/<pk>/', DeleteItemView.as_view(), name='delete_item'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
)