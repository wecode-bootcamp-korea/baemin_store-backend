# Generated by Django 3.1.5 on 2021-01-20 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_auto_20210121_0111'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stocks',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='on_stock', to='product.stock'),
        ),
    ]