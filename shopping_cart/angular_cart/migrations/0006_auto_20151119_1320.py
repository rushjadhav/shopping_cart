# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('angular_cart', '0005_remove_product_specifications'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productordermap',
            name='price',
        ),
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateField(auto_now_add=True, verbose_name=b'Order Date'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(default=b'N', max_length=1, choices=[(b'C', b'Completed'), (b'N', b'Not Completed')]),
        ),
    ]
