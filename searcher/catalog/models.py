from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=256, verbose_name='Наименование')
    provider = models.CharField(max_length=100, verbose_name='Поставщик')
    price_for_unit = models.IntegerField(verbose_name='Цена за еденицу товара')
    unit_type = models.CharField(max_length=20, verbose_name='Единица измерения')
    in_box = models.CharField(max_length=20, verbose_name='Единица измерения в коробке', null=True)
    country = models.CharField(max_length=20, verbose_name='Страна-изготовитель', null=True)
    code = models.IntegerField(verbose_name='Код товара', null=True)


    class Meta:
        verbose_name = ("Продукт")
        verbose_name_plural = ("Продукты")

    def __str__(self):
        return self.title

