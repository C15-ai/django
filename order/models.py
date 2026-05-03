from django.db import models

class Order(models.Model):
    customer_name = models.CharField(max_length=100)
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.customer_name} - {self.product_name}"
