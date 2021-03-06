# Generated by Django 3.1.5 on 2021-01-20 09:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_auto_20210120_1739'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='is_on_sale',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='on_sale',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.sale'),
        ),
    ]
