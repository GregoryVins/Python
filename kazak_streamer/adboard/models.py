from django.contrib.auth.models import User
from django.db import models

from .cities import CITIES


class AdCategory(models.Model):
    """Модель категорий объявлений."""
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)
    image = models.ImageField(upload_to='AdCategory_images', blank=True)

    def __str__(self):
        return self.name

    def get_ads_count(self):
        return Ad.objects.filter(ad_category__name=self.name).count()


class Ad(models.Model):
    """Модель объявления."""
    ad_category = models.ForeignKey(AdCategory, verbose_name='Категория', on_delete=models.CASCADE)
    author = models.ForeignKey(User, verbose_name='Автор объявления', on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True)
    price = models.PositiveIntegerField(default=0)
    city = models.CharField(choices=CITIES, max_length=64, default=0)
    year = models.PositiveIntegerField(default=2020, blank=True)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} ({self.ad_category.name})'
