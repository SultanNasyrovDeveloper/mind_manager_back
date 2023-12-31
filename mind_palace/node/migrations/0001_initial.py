# Generated by Django 4.0.5 on 2022-10-08 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NodeBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('chess', 'CHESS'), ('code', 'CODE'), ('text', 'TEXT'), ('translation', 'TRANSLATION')], default='text', max_length=50)),
                ('meta', models.JSONField(default=dict)),
                ('data', models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='NodeMedia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('image', 'IMAGE'), ('not_set', 'NOT_SET'), ('youtube', 'YOUTUBE')], default='not_set', max_length=100)),
                ('title', models.CharField(default=None, max_length=500, null=True)),
                ('description', models.TextField(default=None, null=True)),
                ('image', models.ImageField(upload_to='node_media/')),
                ('config', models.JSONField(default=dict)),
            ],
        ),
        migrations.CreateModel(
            name='NodeTag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='PalaceNode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, verbose_name='Name')),
                ('description', models.TextField(blank=True, default='', null=True, verbose_name='Description')),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
