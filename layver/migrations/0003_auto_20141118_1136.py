# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('layver', '0002_screen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='screenshot',
            name='page',
        ),
        migrations.DeleteModel(
            name='ScreenShot',
        ),
    ]
