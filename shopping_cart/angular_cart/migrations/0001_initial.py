# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=80, verbose_name=b'Name')),
                ('description', models.TextField(null=True, verbose_name=b'Description', blank=True)),
                ('status', models.CharField(default=b'A', help_text=b'Only active categories are shown on site.', max_length=1, verbose_name=b'Status', choices=[(b'A', b'Active'), (b'I', b'Inactive')])),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('shipping_address', models.TextField(verbose_name=b'Shipping Address')),
                ('order_date', models.DateField(verbose_name=b'Order Date')),
                ('delivery_date', models.DateField(null=True, verbose_name=b'Delivered on', blank=True)),
                ('status', models.CharField(max_length=1, choices=[(b'C', b'Completed'), (b'N', b'Not Completed')])),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=80, verbose_name=b'Name')),
                ('price', models.DecimalField(verbose_name=b'Price', max_digits=10, decimal_places=5)),
                ('description', models.TextField(null=True, verbose_name=b'Description', blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'', blank=True)),
                ('status', models.CharField(default=b'A', max_length=1, verbose_name=b'Status', choices=[(b'A', b'Active'), (b'I', b'Inactive')])),
                ('category', models.ForeignKey(related_name='products', to='angular_cart.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductOrderMap',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('quantity', models.IntegerField()),
                ('price', models.DecimalField(verbose_name=b'Price', max_digits=10, decimal_places=5)),
                ('order', models.ForeignKey(to='angular_cart.Order')),
                ('product', models.ForeignKey(to='angular_cart.Product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(to='angular_cart.Product', through='angular_cart.ProductOrderMap'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(related_name='orders', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='product',
            unique_together=set([('name', 'category')]),
        ),
    ]
