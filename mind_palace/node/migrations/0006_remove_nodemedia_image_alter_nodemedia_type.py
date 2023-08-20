# Generated by Django 4.1.3 on 2023-08-04 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0005_alter_nodebody_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nodemedia',
            name='image',
        ),
        migrations.AlterField(
            model_name='nodemedia',
            name='type',
            field=models.CharField(choices=[('not_set', 'not_set'), ('youtube', 'youtube')], default='not_set', max_length=100),
        ),
    ]
