# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('angular_cart', '0004_product_specifications'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='specifications',
        ),
    ]
