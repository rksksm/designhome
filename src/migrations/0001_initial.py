# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import src.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('pic', models.FileField(upload_to=src.models.generate_filename)),
            ],
        ),
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('pic1', models.FileField(upload_to=src.models.generate_filename51)),
                ('pic2', models.FileField(upload_to=src.models.generate_filename52)),
                ('pic3', models.FileField(upload_to=src.models.generate_filename53)),
                ('pic5', models.FileField(upload_to=src.models.generate_filename55)),
                ('pic6', models.FileField(upload_to=src.models.generate_filename56)),
                ('pic7', models.FileField(upload_to=src.models.generate_filename57)),
                ('pic8', models.FileField(upload_to=src.models.generate_filename58)),
                ('pic9', models.FileField(upload_to=src.models.generate_filename59)),
                ('pic10', models.FileField(upload_to=src.models.generate_filename510)),
                ('pic11', models.FileField(upload_to=src.models.generate_filename511)),
                ('pic12', models.FileField(upload_to=src.models.generate_filename512)),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('pic1', models.FileField(upload_to='generate_filename11')),
                ('pic2', models.FileField(upload_to='generate_filename12')),
                ('pic3', models.FileField(upload_to='generate_filename13')),
                ('pic4', models.FileField(upload_to='generate_filename14')),
                ('pic5', models.FileField(upload_to='generate_filename15')),
                ('pic6', models.FileField(upload_to='generate_filename16')),
                ('pic7', models.FileField(upload_to='generate_filename17')),
                ('pic8', models.FileField(upload_to='generate_filename18')),
            ],
        ),
        migrations.CreateModel(
            name='Icon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('pic1', models.FileField(upload_to=src.models.generate_filename61)),
                ('pic2', models.FileField(upload_to=src.models.generate_filename62)),
                ('pic3', models.FileField(upload_to=src.models.generate_filename63)),
                ('pic5', models.FileField(upload_to=src.models.generate_filename65)),
                ('pic6', models.FileField(upload_to=src.models.generate_filename66)),
                ('pic7', models.FileField(upload_to=src.models.generate_filename67)),
                ('pic8', models.FileField(upload_to=src.models.generate_filename68)),
                ('pic9', models.FileField(upload_to=src.models.generate_filename69)),
                ('pic10', models.FileField(upload_to=src.models.generate_filename610)),
                ('pic11', models.FileField(upload_to=src.models.generate_filename611)),
                ('pic12', models.FileField(upload_to=src.models.generate_filename612)),
            ],
        ),
        migrations.CreateModel(
            name='Interior',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('pic1', models.FileField(upload_to=src.models.generate_filename41)),
                ('pic2', models.FileField(upload_to=src.models.generate_filename42)),
                ('pic3', models.FileField(upload_to=src.models.generate_filename43)),
                ('pic4', models.FileField(upload_to=src.models.generate_filename44)),
                ('pic5', models.FileField(upload_to=src.models.generate_filename45)),
                ('pic6', models.FileField(upload_to=src.models.generate_filename46)),
                ('pic7', models.FileField(upload_to=src.models.generate_filename47)),
                ('pic8', models.FileField(upload_to=src.models.generate_filename48)),
                ('pic9', models.FileField(upload_to=src.models.generate_filename49)),
                ('pic10', models.FileField(upload_to=src.models.generate_filename410)),
                ('pic11', models.FileField(upload_to=src.models.generate_filename411)),
                ('pic12', models.FileField(upload_to=src.models.generate_filename412)),
            ],
        ),
        migrations.CreateModel(
            name='Recent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('recent_works', models.CharField(max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('pic1', models.FileField(upload_to=src.models.generate_filename31)),
                ('pic2', models.FileField(upload_to=src.models.generate_filename32)),
                ('pic3', models.FileField(upload_to=src.models.generate_filename33)),
                ('pic4', models.FileField(upload_to=src.models.generate_filename34)),
                ('pic5', models.FileField(upload_to=src.models.generate_filename35)),
                ('pic6', models.FileField(upload_to=src.models.generate_filename36)),
            ],
        ),
    ]
