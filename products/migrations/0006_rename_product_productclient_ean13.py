# Generated by Django 4.2.4 on 2023-08-22 18:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_alter_product_name_prep'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productclient',
            old_name='product',
            new_name='ean13',
        ),
    ]
