from django.db import models

# Create your models here.


class ShopingItem(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    price = models.IntegerField()
    discount = models.IntegerField()
    expirydate = models.DateTimeField(null=True)

    def __str__(self):
        return self.name
