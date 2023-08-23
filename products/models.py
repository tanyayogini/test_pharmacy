from django.contrib import admin
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class Product(models.Model):
    ean13 = models.CharField(primary_key=True, max_length=255, verbose_name='Штрих-код')
    name_prep = models.CharField(max_length=255, verbose_name='Наименование товара')

    def __str__(self):
        return self.ean13

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'


class ProductClient(models.Model):
    ean13 = models.ForeignKey(Product, on_delete=models.PROTECT, verbose_name='Штрих-код', related_name='names')
    name_prep = models.CharField(max_length=255, verbose_name='Пользовательское наименование товара')

    def __str__(self):
        return self.ean13.name_prep

    class Meta:
        verbose_name = 'Пользовательский товар'
        verbose_name_plural = 'Пользовательские товары'



class Distribution(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE, verbose_name='Товар', blank=True)

    def __str__(self):
        return self.product.ean13

    class Meta:
        verbose_name = 'Стыковка товаров'
        verbose_name_plural = 'Стыковка товаров'


    @admin.display(description='Пользовательские названия')
    def names(self):
        self.names = self.product.names.all()
        return list(client_name for client_name in self.names)

    @admin.display(description='Количество записей клиентов')
    def count_names(self):
        return self.names.count()


@receiver(post_save, sender=Product)
def create_product(sender, instance, created, **kwargs):
    if created:
        Distribution.objects.create(product=instance)
