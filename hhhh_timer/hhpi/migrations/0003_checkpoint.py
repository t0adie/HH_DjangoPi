# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hhpi', '0002_auto_20150812_1722'),
    ]

    operations = [
        migrations.CreateModel(
            name='Checkpoint',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('bib_id', models.IntegerField()),
                ('course_id', models.IntegerField()),
                ('cp_id', models.IntegerField()),
                ('cp_timestamp', models.TimeField(auto_now_add=True, verbose_name=b'timecheck')),
            ],
        ),
    ]
