# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hhpi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rider',
            name='bib_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='rider',
            name='course_id',
            field=models.IntegerField(),
        ),
    ]
