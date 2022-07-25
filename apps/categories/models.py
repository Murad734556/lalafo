from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(verbose_name="Самогенерация URL адреса")

    def __str__(self):
        return f"{self.title}" 

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    class MPTTMeta:
        order_insertion_by=['title']


class ChildCategory(models.Model):
    parent = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="category_parent")
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(verbose_name="Человекопонятный URL (само генерация)")


    def __str__(self):
        return f"Категория {self.parent.title}, подкатегория {self.title}"

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"