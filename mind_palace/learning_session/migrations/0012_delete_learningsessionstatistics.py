# Generated by Django 4.1.3 on 2023-08-10 18:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_session', '0011_noderepetition'),
    ]

    operations = [
        migrations.DeleteModel(
            name='LearningSessionStatistics',
        ),
    ]