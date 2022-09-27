from .models import ShopingItem
from .serializers import ShoppinItemSerializers
from rest_framework import viewsets


class ShoppingViewset(viewsets.ModelViewSet):
    queryset = ShopingItem.objects.all()
    serializer_class = ShoppinItemSerializers
