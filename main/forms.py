from django.forms import ModelForm
from main.models import Product
from django.utils.html import strip_tags
from django.core.exceptions import ValidationError

class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = [
            'name',
            'price',
            'description',
            'thumbnail',
            'category',
            'is_featured',
        ]

    def clean_name(self):
        name = self.cleaned_data.get("name", "")
        return strip_tags(name).strip()

    def clean_description(self):
        description = self.cleaned_data.get("description", "")
        return strip_tags(description).strip()

    def clean_price(self):
        price = self.cleaned_data.get("price", 0)
        try:
            price = int(price)
        except (TypeError, ValueError):
            raise ValidationError("Enter a valid price.")
        if price < 0:
            raise ValidationError("Price must be zero or positive.")
        return price

    def clean_thumbnail(self):
        thumbnail = self.cleaned_data.get("thumbnail", "")
        return strip_tags(thumbnail).strip()