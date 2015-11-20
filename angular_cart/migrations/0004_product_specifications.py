# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('angular_cart', '0003_auto_20151118_1440'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='specifications',
            field=models.TextField(help_text=b"Please store values in json format                                               e.g {'screen': 5.6, 'battery': 2 amp}", null=True, verbose_name=b'Specifications', blank=True),
        ),
    ]
