# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('layver', '0004_markerrors'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='browser1',
            field=models.CharField(max_length=15, default='ie'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='page',
            name='browser2',
            field=models.CharField(max_length=15, default='firefox'),
            preserve_default=False,
        ),
    ]
