from django import forms
from django.forms import ModelForm
from .models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"

    def clean_price(self):
        price = self.cleaned_data["price"]
        if price > 1000:
            msg = "Product is too expensive"
            raise forms.ValidationError(msg)
        return price

    def clean_description(self):
        desc = self.cleaned_data["description"]
        if len(desc) <= 20:
            msg = "Product must have a good description"
            raise forms.ValidationError(msg)
        return desc
