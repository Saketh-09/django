from .viewset import ShoppingViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('restapi', ShoppingViewset, basename='shopping')

for url in router.urls:
    print(url, '\n')
