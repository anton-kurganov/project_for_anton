from django.db import models


class Provider(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Имя поставщика'
    )
    number = models.CharField(
        max_length=20,
        verbose_name='Номер телефона',
        blank=True
    )
    email = models.CharField(
        max_length=50,
        verbose_name='Email',
        blank=True
    )
    url = models.URLField(
        verbose_name='Сайт поставщика',
        blank=True
    )
    brand = models.CharField(
        max_length=25,
        verbose_name='Бренд'
    )

    class Meta:
        verbose_name = "Поставщик"
        verbose_name_plural = "Поставщики"

    def __str__(self):
        return self.name


class Product(models.Model):
    title = models.CharField(
        max_length=256,
        verbose_name='Наименование'
    )
    search_field = models.CharField(
        max_length=256,
        verbose_name='Поисковая строка'
    )
    provider = models.ForeignKey(
        Provider,
        on_delete=models.CASCADE,
        verbose_name='Поставщик'
    )
    price_for_unit = models.CharField(
        max_length=50,
        verbose_name='Цена за еденицу товара'
    )
    unit_type = models.CharField(
        max_length=20,
        verbose_name='Единица измерения'
    )
    in_box = models.CharField(
        max_length=20,
        verbose_name='Единица измерения в коробке',
        blank=True
    )
    country = models.CharField(
        max_length=100,
        verbose_name='Страна-изготовитель',
        blank=True
    )
    code = models.CharField(
        max_length=40,
        verbose_name='Код товара',
        blank=True
    )

    class Meta:
        verbose_name = ("Продукт")
        verbose_name_plural = ("Продукты")

    def __str__(self):
        return self.title
