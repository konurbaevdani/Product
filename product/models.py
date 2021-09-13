from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(primary_key=True)

    created_at = models.DateField("Дата создания", auto_now_add=True)
    updated_at = models.DateField("Дата редактирования", auto_now=True)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Category'


class Product(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    price = models.IntegerField()
    category = models.ForeignKey(Category,
                                    on_delete=models.CASCADE,
                                    related_name='reviews',
                                    verbose_name='category')
    created_at = models.DateTimeField("Дата создания", auto_now_add=True)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Product'





