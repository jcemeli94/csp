# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cspapp', '0003_auto_20160511_1116'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='answer',
            name='title',
        ),
        migrations.AlterField(
            model_name='answer',
            name='body',
            field=models.TextField(),
        ),
    ]
