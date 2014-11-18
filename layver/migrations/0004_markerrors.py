# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('layver', '0003_auto_20141118_1136'),
    ]

    operations = [
        migrations.CreateModel(
            name='MarkErrors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_browser1', models.ImageField(upload_to='marks/')),
                ('image_browser2', models.ImageField(upload_to='marks/')),
                ('page', models.ForeignKey(to='layver.Page')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
