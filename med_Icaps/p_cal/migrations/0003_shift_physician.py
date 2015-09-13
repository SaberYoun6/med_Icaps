# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('p_cal', '0002_remove_shift_shift_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='shift',
            name='physician',
            field=models.CharField(max_length=200, default='Mazin Elsarrag'),
            preserve_default=False,
        ),
    ]
