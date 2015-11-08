# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import src.models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0002_building_pic4'),
    ]

    operations = [
        migrations.AddField(
            model_name='icon',
            name='pic4',
            field=models.FileField(upload_to=src.models.generate_filename64, default=1),
            preserve_default=False,
        ),
    ]
