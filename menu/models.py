from django.db import models

class MenuCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Dish(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    category = models.ForeignKey('menu.Dish', on_delete=models.CASCADE)
    available = models.BooleanField(default=True)


    def __str__(self):
        return self.name