from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.urls import reverse

User = get_user_model()


class Category(models.Model):
    """Модель категорий товаров"""
    title = models.CharField(max_length=30)
    slug = models.SlugField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("store:subcategory", kwargs={"category_slug": self.slug})


class SubCategory(models.Model):
    """Модель подкатегорий товаров"""
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, null=True
    )
    title = models.CharField(max_length=30)
    slug = models.SlugField(null=True, blank=True)
    sub_image = models.ImageField(
        blank=True, upload_to='subimages/',
        verbose_name='Изображение подкатегории'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("store:store", kwargs={"subCategory_slug": self.slug})


class Product(models.Model):
    """Модель товаров, включающая все характеристики"""
    subCategory = models.ForeignKey(
        SubCategory, on_delete=models.CASCADE, null=True
    )
    title = models.CharField(max_length=100)
    slug = models.SlugField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    detail = models.TextField(null=True, blank=True)
    articul = models.CharField(max_length=16, default="00000000")
    country = models.CharField(max_length=45, null=True, blank=True)
    price = models.IntegerField()
    discount_price = models.IntegerField(default=0)
    quantity = models.IntegerField(null=True)
    time_create = models.DateTimeField(
        auto_now_add=True, verbose_name='Время создания'
        )
    brand = models.CharField(max_length=45, null=True, blank=True)
    image0 = models.ImageField(
        blank=True, upload_to='images/',
        verbose_name='Главное изображение'
    )
    image1 = models.ImageField(
        blank=True, null=True, upload_to='images/',
        verbose_name='Доп Изображение 1'
    )
    image2 = models.ImageField(
        blank=True, null=True, upload_to='images/',
        verbose_name='Доп Изображение 2'
    )
    image3 = models.ImageField(
        blank=True, null=True, upload_to='images/',
        verbose_name='Доп Изображение 3'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("store:product", kwargs={"product_slug": self.slug})

    def sale(self):
        discount = int(100 - (100 * self.discount_price) / self.price)
        return discount


class Review(models.Model):
    author = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name='reviews',
        to=User,
        verbose_name='Автор',
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )
    score = models.IntegerField(
        validators=[
            MinValueValidator(settings.MIN_LIMIT_VALUE),
            MaxValueValidator(settings.MAX_LIMIT_VALUE)
        ],
    )
    text = models.TextField(null=True, blank=True)
    product = models.ForeignKey(
        on_delete=models.CASCADE,
        related_name='product',
        to='Product',
        verbose_name='Товар'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'product'],
                name='unique_review'
            )
        ]
        ordering = ('pub_date',)
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'

    def __str__(self):
        return self.text[:settings.LIMIT_REVIEW_STR]
