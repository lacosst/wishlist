from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    title = models.CharField(max_length=120, verbose_name='Заголовок')
    link = models.URLField(verbose_name='URL')
    price = models.IntegerField(verbose_name='Цена')
    create = models.DateTimeField(auto_now_add=True)
    # update = models.DateTimeField(auto_now=)

    def __str__(self):
        return self.title


class WishList(models.Model):
    """ таблица "Лист желаний"
    id
    owner
    products - ManyToMany
    is_hidden - bool
    """
    title = models.CharField(max_length=120)
    products = models.ManyToManyField(Product)
    is_hidden = models.BooleanField(default=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
