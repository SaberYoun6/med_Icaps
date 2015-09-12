# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Physician',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name_first', models.CharField(max_length=200)),
                ('name_last', models.CharField(max_length=200)),
                ('specialty', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Shift',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('shift_time_start', models.DateTimeField(verbose_name='Shift Start Time')),
                ('shift_time_end', models.DateTimeField(verbose_name='Shift End Time')),
                ('shift_location', models.CharField(max_length=200)),
                ('shift_date', models.DateTimeField(verbose_name='Shift Date')),
            ],
        ),
    ]
