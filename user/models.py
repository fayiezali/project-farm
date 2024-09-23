from django.db import models
from decimal import Decimal
from django.contrib.auth.models import User 
from django.utils.timezone import now


class Customer(models.Model):
    """Model to store customer information"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=20)
    address = models.TextField()
    city = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)

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
        return self.user.username
