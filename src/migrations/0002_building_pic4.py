# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import src.models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='building',
            name='pic4',
            field=models.FileField(default=1, upload_to=src.models.generate_filename54),
            preserve_default=False,
        ),
    ]
