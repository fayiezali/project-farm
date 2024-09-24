from django.db import models
#
#
class Coupon(models.Model):
    """Model to store coupon information"""
    code = models.CharField(max_length=50, unique=True)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    active = models.BooleanField(default=True)
    expires_at = models.DateTimeField()

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
        return f"Coupon {self.code} - {self.discount}%"
