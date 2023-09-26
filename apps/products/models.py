from django.db import models
from django.utils.text import slugify

from apps.common.models import BaseModel


class Product(BaseModel):
    category = models.ForeignKey('products.Category', on_delete=models.CASCADE, null=True,)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(blank=True, null=True, help_text="Aksiya bo'layokan vaqtda, eski narxi yozilishi mumkin")
    is_available = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['-created_time']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class Category(BaseModel):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True, blank=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save()
