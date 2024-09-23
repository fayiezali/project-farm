# from django.db import models
# from decimal import Decimal
# from django.contrib.auth.models import User 
# from django.utils.timezone import now



# class Category(models.Model):
#     """Model to categorize products"""
#     name = models.CharField(max_length=255)
#     slug = models.SlugField(unique=True)

#     @classmethod
#     def create(cls, **kwargs):
#         return cls.objects.create(**kwargs)

#     @classmethod
#     def read(cls, pk):
#         return cls.objects.get(pk=pk)

#     @classmethod
#     def update(cls, pk, **kwargs):
#         obj = cls.objects.get(pk=pk)
#         for key, value in kwargs.items():
#             setattr(obj, key, value)
#         obj.save()
#         return obj

#     @classmethod
#     def delete(cls, pk):
#         obj = cls.objects.filter(pk=pk)
#         obj.delete()
#         return None

#     @classmethod
#     def all(cls):
#         return cls.objects.all()

#     @classmethod
#     def search(cls, **kwargs):
#         return cls.objects.filter(**kwargs)

#     def __str__(self):
#         return self.name




# class Product(models.Model):
#     """Model to store product information"""
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     price = models.DecimalField(max_digits=10, decimal_places=2)
#     stock = models.PositiveIntegerField()
#     category = models.ForeignKey(Category, related_name='products',
#                                  on_delete=models.CASCADE)
#     image = models.ImageField(upload_to='products/', null=True, blank=True)

#     @classmethod
#     def create(cls, **kwargs):
#         return cls.objects.create(**kwargs)

#     @classmethod
#     def read(cls, pk):
#         return cls.objects.get(pk=pk)

#     @classmethod
#     def update(cls, pk, **kwargs):
#         obj = cls.objects.get(pk=pk)
#         for key, value in kwargs.items():
#             setattr(obj, key, value)
#         obj.save()
#         return obj

#     @classmethod
#     def delete(cls, pk):
#         obj = cls.objects.filter(pk=pk)
#         obj.delete()
#         return None

#     @classmethod
#     def all(cls):
#         return cls.objects.all()

#     @classmethod
#     def search(cls, **kwargs):
#         return cls.objects.filter(**kwargs)

#     def __str__(self):
#         return self.title

