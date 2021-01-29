# Generated by Django 3.1.5 on 2021-01-20 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_auto_20210120_1817'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='on_sale',
            new_name='on_sales',
        ),
        migrations.RenameField(
            model_name='sale',
            old_name='sales_rate',
            new_name='rate',
        ),
        migrations.RemoveField(
            model_name='sale',
            name='is_on_sale',
        ),
    ]
