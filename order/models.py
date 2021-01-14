from django.db import models


class Order(models.Model):
    user          = models.ForeignKey('user.User',   on_delete=models.CASCADE)
    order_status  = models.ForeignKey('OrderStatus', on_delete=models.CASCADE)
    create_at     = models.DateField(auto_now_add=True)
    update_at     = models.DateField(auto_now=True)
    

    class Meta:
      db_table = 'orders'


class OrderStatus(models.Model):
    order_id  = models.IntegerField(default=0)
    status    = models.CharField(max_length=45)

    class Meta:
      db_table = 'order_status'


class OrderItem(models.Model):
    address     = models.ForeignKey('user.Address', on_delete=models.CASCADE)
    product     = models.ForeignKey('product.Product', on_delete=models.CASCADE)
    order       = models.ForeignKey('Order', on_delete=models.CASCADE)
    quantity    = models.IntegerField(default=0)
    total_price = models.DecimalField(max_digits=18, decimal_places=2)

    class Meta:
      db_table = 'order_items'