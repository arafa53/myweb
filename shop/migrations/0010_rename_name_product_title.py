# Generated by Django 4.1.2 on 2022-11-06 10:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_rename_title_product_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='title',
        ),
    ]
