# Generated by Django 4.0.5 on 2022-06-02 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_delete_discounts'),
        ('accounts', '0002_remove_userprofile_address2'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='product_favorites',
            field=models.ManyToManyField(to='products.product'),
        ),
    ]
