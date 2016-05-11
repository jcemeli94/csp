# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cspapp', '0002_auto_20160511_1006'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='body',
            new_name='description',
        ),
    ]
