# Generated by Django 4.1.3 on 2023-08-10 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_session', '0012_delete_learningsessionstatistics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userlearningsession',
            name='repeated_nodes',
        ),
    ]
