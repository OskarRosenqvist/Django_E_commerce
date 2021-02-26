from django.contrib import admin
from .models import Product, OrderItem, Order, FormatVariation, PriceVariables

admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(FormatVariation)
admin.site.register(PriceVariables)
