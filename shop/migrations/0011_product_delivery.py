# Generated by Django 4.1.2 on 2022-11-10 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_rename_name_product_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='delivery',
            field=models.IntegerField(null=True),
        ),
    ]
