# Generated by Django 4.2.4 on 2023-08-22 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_rename_name_product_name_prep_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='name_prep',
            field=models.CharField(max_length=255, verbose_name='Наименование товара'),
        ),
    ]
