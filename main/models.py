from django.db import models


class Product(models.Model):
    title = models.CharField(max_length=120, verbose_name='Заголовок')
    link = models.URLField(verbose_name='URL')
    price = models.IntegerField(verbose_name='Цена')
    create = models.DateTimeField(auto_now_add=True)
    # update = models.DateTimeField(auto_now=)

    def __str__(self):
        return self.title
