from django.db import models


class Category(models.Model):
    """Модель категорий товаров"""
    title = models.CharField(max_length=30)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title


class SubCategory(models.Model):
    """Модель подкатегорий товаров"""
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True
    )
    title = models.CharField(max_length=30)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title


class Product(models.Model):
    """Модель товаров, включающая все характеристики"""
    subCategory = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, null=True
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    articul = models.CharField(max_length=16, default="00000000")
    country = models.CharField(max_length=45, null=True, blank=True)
    price = models.IntegerField()
    quantity = models.IntegerField(null=True)
    image0 = models.ImageField(
        blank=True, upload_to='media/images/',
        verbose_name='Главное изображение'
    )
    image1 = models.ImageField(
        blank=True, upload_to='media/images/',
        verbose_name='Доп Изображение 1'
    )
    image2 = models.ImageField(
        blank=True, upload_to='media/images/',
        verbose_name='Доп Изображение 2'
    )
    image3 = models.ImageField(
        blank=True, upload_to='media/images/',
        verbose_name='Доп Изображение 3'
    )

    def __str__(self):
        return self.title
