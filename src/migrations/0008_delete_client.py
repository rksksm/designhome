# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0007_client'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Client',
        ),
    ]
