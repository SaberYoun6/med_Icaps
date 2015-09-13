# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('p_cal', '0003_shift_physician'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Specialty',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
            ],
        ),
        migrations.RenameField(
            model_name='shift',
            old_name='shift_location',
            new_name='location',
        ),
        migrations.RemoveField(
            model_name='shift',
            name='shift_time_end',
        ),
        migrations.RemoveField(
            model_name='shift',
            name='shift_time_start',
        ),
        migrations.AddField(
            model_name='shift',
            name='time_end',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 13, 3, 50, 47, 967367, tzinfo=utc), verbose_name='End Time'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shift',
            name='time_start',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Start Time'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='physician',
            name='id',
            field=models.AutoField(serialize=False, primary_key=True),
        ),
    ]
