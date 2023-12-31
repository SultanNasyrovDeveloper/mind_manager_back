# Generated by Django 4.0.5 on 2022-10-08 15:40

import datetime
import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('node', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserLearningSession',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('active', 'active'), ('finished', 'finished')], default='active', max_length=100)),
                ('strategy_name', models.CharField(choices=[('sm2', 'supermemo_2')], default='sm2', max_length=1000)),
                ('queue', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=list, size=None)),
                ('average_rating', models.FloatField(default=0)),
                ('total_repetitions', models.PositiveSmallIntegerField(default=0)),
                ('repeated_nodes', django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=list, size=None)),
                ('start_datetime', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('finish_datetime', models.DateTimeField(default=None, null=True)),
                ('last_repetition_datetime', models.DateTimeField(default=datetime.datetime.utcnow)),
                ('root', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='node.palacenode')),
            ],
        ),
    ]
