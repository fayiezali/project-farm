from django.db import models
from user.models import Customer
from product.models import  Product
#
#
class CartItem(models.Model):
    """Model to represent items added to the cart"""
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    @classmethod
    def create(cls, **kwargs):
        return cls.objects.create(**kwargs)

    @classmethod
    def read(cls, pk):
        return cls.objects.get(pk=pk)

    @classmethod
    def update(cls, pk, **kwargs):
        obj = cls.objects.get(pk=pk)
        for key, value in kwargs.items():
            setattr(obj, key, value)
        obj.save()
        return obj

    @classmethod
    def delete(cls, pk):
        obj = cls.objects.filter(pk=pk)
        obj.delete()
        return None

    @classmethod
    def all(cls):
        return cls.objects.all()

    @classmethod
    def search(cls, **kwargs):
        return cls.objects.filter(**kwargs)

    def __str__(self):
        return f"{self.product.title} - {self.quantity}"

