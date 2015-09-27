# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rider',
            fields=[
                ('id', models.IntegerField(serialize=False, primary_key=True)),
                ('firstname', models.CharField(max_length=50)),
                ('lastname', models.CharField(max_length=50)),
                ('bib_id', models.IntegerField(max_length=3)),
                ('course_id', models.IntegerField(max_length=1)),
            ],
        ),
    ]
