from django.db import models

class User(models.Model):
    account      = models.CharField(max_length=45)
    password     = models.CharField(max_length=255)
    name         = models.CharField(max_length=50)
    email        = models.EmailField(max_length=45)
    phone        = models.CharField(max_length=11)
    create_at    = models.DateField(auto_now_add=True)
    update_at    = models.DateField(auto_now=True)
    liked        = models.ManyToManyField('product.Product', through='product.Like',null=True)


    class Meta:
      db_table = 'users'


class Address(models.Model):
    user     = models.ForeignKey('User', on_delete=models.CASCADE, related_name='addresses', null=True)
    name     = models.CharField(max_length=100)
    receiver = models.CharField(max_length=45)

    class Meta:
      db_table = 'addresses'

class Coupon(models.Model):
    user        = models.ForeignKey('User', on_delete=models.CASCADE)
    min_ammount = models.DecimalField(max_digits=18, decimal_places=2)
    coupon_rate = models.DecimalField(max_digits=3, decimal_places=2)
    name        = models.CharField(max_length=45)
    create_at   = models.DateField(auto_now_add=True)
    update_at   = models.DateField(auto_now_add=True)

    class Meta:
      db_table= 'coupons'