# Generated by Django 4.1.2 on 2022-10-28 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_category_main_category_sub_category_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sub_category',
            name='category',
        ),
        migrations.AddField(
            model_name='sub_category',
            name='main_category',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='shop.main_category'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
