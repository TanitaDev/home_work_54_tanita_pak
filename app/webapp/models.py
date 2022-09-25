from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=200, null=False, verbose_name="Наименование категории")
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Описание")


class Product(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False, verbose_name="Наименование товара")
    description = models.TextField(max_length=3000, null=True, blank=True, verbose_name="Описание")
    create_at = models.DateTimeField(auto_now_add=True, verbose_name="Время создания")
    price = models.DecimalField(max_digits=10, decimal_places=0, verbose_name="Цена товара")
    category = models.ForeignKey(verbose_name='Наименование категории', to="Category", on_delete=models.CASCADE, null=True, related_name="Категории")
    image = models.URLField(verbose_name="Изображение товара")

