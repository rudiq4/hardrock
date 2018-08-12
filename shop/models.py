from django.db import models
from django.core.urlresolvers import reverse


class Category(models.Model):
    name = models.CharField(
        max_length=32,
        db_index=True
    )
    slug = models.SlugField(
        max_length=32,
        db_index=True,
        unique=True
    )

    class Meta:
        verbose_name = 'Категорія'
        verbose_name_plural = 'Категорії'

    def __str__(self):
        return "%s" % self.name

    def get_absolute_url(self):
        return reverse('shop:ProductListByCategory', args=[self.slug])





class Product(models.Model):
    category = models.ForeignKey(
        Category,
        related_name='products',
        verbose_name='Категорія'
    )
    name = models.CharField(
        max_length=32,
        db_index=True,
        verbose_name='Назва'
    )
    slug = models.SlugField(
        max_length=32,
        db_index=True
    )
    image = models.ImageField(
        upload_to='prod_img/',
        blank=True,
        verbose_name='Зображення'
    )
    desc = models.TextField(
        blank=True,
        verbose_name='Опис'
    )
    short_desc = models.TextField(
        blank=True,
        verbose_name='Короткий опис'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Ціна'
    )
    stock = models.PositiveIntegerField(
        verbose_name='Запас'
    )
    available = models.BooleanField(
        default=True,
        verbose_name='Наявність'
    )
    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Створено')
    updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Оновлено')

    class Meta:
        ordering = ['name']
        index_together = [
            ['id', 'slug']
        ]
        verbose_name = 'Товар'
        verbose_name_plural = 'Товари'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:ProductDetail', args=[self.id, self.slug])


