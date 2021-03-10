from django.urls import path
from .views import (
    ProductListView,
    ProductDetailView,
    CartView,
    IncreaseQuantityView,
    DecreaseQuantityView,
    DeleteItemView,
    CheckoutView,
    PaymentView,
    ThankYouView,
    ConfirmOrderView,
    OrderDetailView,
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
    path('payment/', PaymentView.as_view(), name='payment'),
    path('thanks/', ThankYouView.as_view(), name='thank-you'),
    path('confirm-order/', ConfirmOrderView.as_view(), name='confirm-order'),
    path('orders/<pk>/', OrderDetailView.as_view(), name='order-detail'),
)