# Generated by Django 2.2 on 2020-07-27 03:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twitterapp', '0007_remove_product_vat_rule'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Order',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
