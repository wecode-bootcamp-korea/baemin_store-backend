# Generated by Django 3.1.5 on 2021-01-13 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
        migrations.AddField(
            model_name='producttag',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='producttag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.tag'),
        ),
        migrations.AddField(
            model_name='productsale',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='productsale',
            name='sale',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.sale'),
        ),
        migrations.AddField(
            model_name='producthashtag',
            name='hashtag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.hashtag'),
        ),
        migrations.AddField(
            model_name='producthashtag',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.category'),
        ),
        migrations.AddField(
            model_name='product',
            name='hashtags',
            field=models.ManyToManyField(through='product.ProductHashTag', to='product.HashTag'),
        ),
        migrations.AddField(
            model_name='product',
            name='sales',
            field=models.ManyToManyField(through='product.ProductSale', to='product.Sale'),
        ),
        migrations.AddField(
            model_name='product',
            name='tags',
            field=models.ManyToManyField(through='product.ProductTag', to='product.Tag'),
        ),
        migrations.AddField(
            model_name='like',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
        migrations.AddField(
            model_name='like',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user'),
        ),
    ]
