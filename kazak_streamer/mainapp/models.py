from django.db import models


class Category(models.Model):
    """Категория"""
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255, blank=True)
    is_active = models.BooleanField(default=True, db_index=True)

    def __str__(self):
        return self.name

    @property
    def get_image(self):
        return Product.objects.filter(category__name=self.name).first().image


class Product(models.Model):
    """Продукт какой либо категории"""
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.CharField(max_length=255, blank=True)
    image = models.ImageField(upload_to='products_image', blank=True)
    price = models.PositiveIntegerField(default=0)
    quantity = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True, db_index=True)

    def __str__(self):
        return f'{self.name} ({self.category.name})'

    @staticmethod
    def get_active_items():
        return Product.objects.filter(category__is_active=True, is_active=True)
