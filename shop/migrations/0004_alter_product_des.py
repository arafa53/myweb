# Generated by Django 4.1.2 on 2022-10-23 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_rename_pub_date_product_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='des',
            field=models.CharField(max_length=2000),
        ),
    ]
