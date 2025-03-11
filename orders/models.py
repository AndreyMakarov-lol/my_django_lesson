from django.db import models
from django.contrib.auth.models import User

from products.models import Product


# Create your models here.
class SalesOrder(models.Model):
    amount = models.IntegerField()
    description = models.CharField(max_length=250)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    #on_delete=
#CASCADE каскадное удаление(удалится пользователь значит удалаятся все его заказы,
#SET_NULL если удалится пользователь то у заказа поле пользователь будет =0
#PROTECT не позволит удалять пользователя пока у него есть заказы
    product = models.ManyToManyField(Product)