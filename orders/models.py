from django.db import models
from django.contrib.auth.models import User
from products import models as product_models


class Order(models.Model):

    products = models.ManyToManyField(product_models.Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()

    def __str__(self):
        return f'Order #{self.pk} by {self.user.username}'
