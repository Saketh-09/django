from django import forms
from .models import ShopingItem
 
 
# creating a form
class ShoppingItemForm(forms.ModelForm):
 
    # create meta class
    class Meta:
        # specify model to be used
        model = ShopingItem
 
        # specify fields to be used
        fields = [
            "name",
            "price",
            "discount",
            "expirydate"
        ]