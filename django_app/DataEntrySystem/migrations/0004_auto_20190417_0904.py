# Generated by Django 2.1.2 on 2019-04-17 09:04

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DataEntrySystem', '0003_auto_20190416_0954'),
    ]

    operations = [
        migrations.AlterField(
            model_name='target_company_package',
            name='company_id_list',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), size=None),
        ),
    ]
