from django.contrib import admin
from .models import Product, OrderItem, Order, FormatVariation, PriceVariables, Address, Payment


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'address_line1',
        'address_line2',
        'city',
        'zip_code',
        'address_type',
    ]


admin.site.register(Product)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(FormatVariation)
admin.site.register(PriceVariables)
admin.site.register(Payment)
admin.site.register(Address, AddressAdmin)
