from django.db import models
from django.contrib.auth.models import User
from menu.models import Dish


class Order(models.Model):
    STATUS_CHOICES = [
        ('PENDING', 'Ожидает'),
        ('IN_PROGRESS', 'Готовится'),
        ('DELIVERED', 'Доставлен'),
        ('CANCELLED', 'Отменён'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"Заказ {self.id} от {self.user.username}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


    def __str__(self):
        return f"{self.quantity} {self.dish.name}"



