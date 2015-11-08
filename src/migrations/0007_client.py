# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0006_auto_20150729_0125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('c1', models.CharField(max_length=140)),
                ('c2', models.CharField(max_length=140)),
                ('c3', models.CharField(max_length=140)),
                ('c4', models.CharField(max_length=140)),
                ('c5', models.CharField(max_length=140)),
                ('c6', models.CharField(max_length=140)),
                ('c7', models.CharField(max_length=140)),
                ('c8', models.CharField(max_length=140)),
                ('c9', models.CharField(max_length=140)),
                ('c10', models.CharField(max_length=140)),
                ('c11', models.CharField(max_length=140)),
                ('c12', models.CharField(max_length=140)),
                ('c13', models.CharField(max_length=140)),
                ('c14', models.CharField(max_length=140)),
                ('c15', models.CharField(max_length=140)),
                ('c16', models.CharField(max_length=140)),
                ('c17', models.CharField(max_length=140)),
                ('c18', models.CharField(max_length=140)),
                ('c19', models.CharField(max_length=140)),
                ('c20', models.CharField(max_length=140)),
                ('c21', models.CharField(max_length=140)),
                ('c22', models.CharField(max_length=140)),
                ('c23', models.CharField(max_length=140)),
                ('c24', models.CharField(max_length=140)),
            ],
        ),
    ]
