from django import forms
from .models import OrderItem, FormatVariation, Product


class AddToCartForm(forms.ModelForm):
    format = forms.ModelChoiceField(queryset=FormatVariation.objects.none())

    class Meta:
        model = OrderItem
        fields = ['quantity', 'format']

    def __init__(self, *args, **kwargs):
        product_id = kwargs.pop('product_id')
        product = Product.objects.get(id=product_id)
        super().__init__(*args, **kwargs)

        self.fields['format'].queryset = product.available_formats.all()


class AddressForm(forms.Form):
    pass
