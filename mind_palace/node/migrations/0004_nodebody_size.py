# Generated by Django 4.1.3 on 2023-01-20 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0003_nodebody_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='nodebody',
            name='size',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
