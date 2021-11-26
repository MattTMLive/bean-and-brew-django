from django.db import models

class Product(models.Model):
    image = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    price = models.IntegerField()

    class Meta:
        db_table = "products"

class Orders(models.Model):
    name = models.CharField(max_length=255)
    order_time = models.DateTimeField()
    status = models.IntegerField()
    coffee = models.ForeignKey(to=Product, on_delete=models.CASCADE)

    class Meta:
        db_table = "orders"