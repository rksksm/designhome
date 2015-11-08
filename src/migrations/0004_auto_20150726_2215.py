# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import src.models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0003_icon_pic4'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=140)),
                ('body', models.TextField()),
                ('date', models.DateTimeField()),
                ('image', models.FileField(upload_to='static/img/blog/')),
                ('pic', models.CharField(default='copy name of image', max_length=75)),
            ],
        ),
        migrations.AlterField(
            model_name='home',
            name='pic1',
            field=models.FileField(upload_to=src.models.generate_filename11),
        ),
        migrations.AlterField(
            model_name='home',
            name='pic2',
            field=models.FileField(upload_to=src.models.generate_filename12),
        ),
        migrations.AlterField(
            model_name='home',
            name='pic3',
            field=models.FileField(upload_to=src.models.generate_filename13),
        ),
        migrations.AlterField(
            model_name='home',
            name='pic4',
            field=models.FileField(upload_to=src.models.generate_filename14),
        ),
        migrations.AlterField(
            model_name='home',
            name='pic5',
            field=models.FileField(upload_to=src.models.generate_filename15),
        ),
        migrations.AlterField(
            model_name='home',
            name='pic6',
            field=models.FileField(upload_to=src.models.generate_filename16),
        ),
        migrations.AlterField(
            model_name='home',
            name='pic7',
            field=models.FileField(upload_to=src.models.generate_filename17),
        ),
        migrations.AlterField(
            model_name='home',
            name='pic8',
            field=models.FileField(upload_to=src.models.generate_filename18),
        ),
    ]
