# from django.db import models
# from decimal import Decimal
# from django.contrib.auth.models import User 
# from django.utils.timezone import now



# class Order(models.Model):
#     """Model to store orders"""
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     total_price = models.DecimalField(max_digits=10, decimal_places=2)
#     created_at = models.DateTimeField(auto_now_add=True)
#     status = models.CharField(max_length=20, choices=[
#         ('pending', 'Pending'),
#         ('processing', 'Processing'),
#         ('shipped', 'Shipped'),
#         ('completed', 'Completed'),
#         ('canceled', 'Canceled')
#     ], default='pending')

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
#         return f"Order {self.id} by {self.customer.user.username}"




# class Checkout(models.Model):
#     """Model to store checkout process information"""
#     customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
#     order = models.OneToOneField(Order, on_delete=models.CASCADE)
#     shipping_address = models.TextField()
#     coupon = models.ForeignKey(Coupon, on_delete=models.SET_NULL, null=True,
#                                blank=True)
#     payment_status = models.CharField(max_length=20, choices=[
#         ('pending', 'Pending'),
#         ('completed', 'Completed'),
#         ('failed', 'Failed')
#     ], default='pending')

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
#         return f"Checkout for Order {self.order.id}"




# class TrackShipment(models.Model):
#     """Model to track shipments"""
#     order = models.OneToOneField(Order, on_delete=models.CASCADE)
#     tracking_number = models.CharField(max_length=100)
#     carrier = models.CharField(max_length=50)
#     status = models.CharField(max_length=100)
#     estimated_delivery = models.DateTimeField()

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
#         return f"Tracking {self.tracking_number} for Order {self.order.id}"




# class Refund(models.Model):
#     """Model to handle refund requests"""
#     order = models.OneToOneField(Order, on_delete=models.CASCADE)
#     reason = models.TextField()
#     status = models.CharField(max_length=20, choices=[
#         ('requested', 'Requested'),
#         ('approved', 'Approved'),
#         ('denied', 'Denied'),
#         ('refunded', 'Refunded')
#     ], default='requested')
#     created_at = models.DateTimeField(auto_now_add=True)

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
#         return f"Refund for Order {self.order.id} - {self.status}"
