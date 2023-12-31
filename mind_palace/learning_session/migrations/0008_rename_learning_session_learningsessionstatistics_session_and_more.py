# Generated by Django 4.1.3 on 2023-07-22 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning_session', '0007_rename_repeated_nodes_learningsessionstatistics_repetitions'),
    ]

    operations = [
        migrations.RenameField(
            model_name='learningsessionstatistics',
            old_name='learning_session',
            new_name='session',
        ),
        migrations.RenameField(
            model_name='userlearningsession',
            old_name='strategy_name',
            new_name='learning_strategy',
        ),
        migrations.RemoveField(
            model_name='userlearningsession',
            name='additional_queue',
        ),
        migrations.AddField(
            model_name='userlearningsession',
            name='queue_generation_strategy',
            field=models.IntegerField(choices=[(3, 'last_repeated_first'), (2, 'outdated_first'), (1, 'random')], default=2),
        ),
    ]
