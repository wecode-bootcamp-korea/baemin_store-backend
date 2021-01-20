from django.db import models

class Order(models.Model):
    user          = models.ForeignKey('user.User',    on_delete=models.CASCADE, related_name='carts')
    order_status  = models.ForeignKey('OrderStatus',  on_delete=models.CASCADE, related_name='carts')
    create_at     = models.DateField(auto_now_add=True)
    
    class Meta:
      db_table = 'orders'


class OrderStatus(models.Model):
    status    = models.CharField(max_length=45)

    class Meta:
      db_table = 'order_status'


class Cart(models.Model):
    address     = models.ForeignKey('user.Address',    on_delete=models.CASCADE, related_name='carts')
    product     = models.ForeignKey('product.Product', on_delete=models.CASCADE, related_name='carts')
    order       = models.ForeignKey('Order',           on_delete=models.CASCADE, related_name='carts', null=True, blank=True)
    total_price = models.DecimalField(max_digits=18,   decimal_places=2)
    thumbnail   = models.ForeignKey('product.Product',   on_delete=models.CASCADE, related_name='cart',  )
    quantity    = models.IntegerField(default=1)

    class Meta:
      db_table = 'carts'