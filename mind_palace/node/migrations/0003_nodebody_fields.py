# Generated by Django 4.1.2 on 2022-10-27 18:15

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("node", "0002_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="nodebody",
            name="fields",
            field=django.contrib.postgres.fields.ArrayField(
                base_field=models.CharField(max_length=1000), default=list, size=None
            ),
        ),
    ]
