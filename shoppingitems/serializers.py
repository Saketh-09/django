from rest_framework import serializers
from .models import ShopingItem


class ShoppinItemSerializers(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShopingItem
        fields = ['name', 'price', 'discount', 'expirydate']
