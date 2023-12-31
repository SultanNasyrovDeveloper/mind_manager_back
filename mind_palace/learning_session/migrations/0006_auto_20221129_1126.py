# Generated by Django 4.1.3 on 2022-11-29 11:26

from django.db import migrations


def create_learning_session_statistics(apps, schema_editor):
    Session = apps.get_model('learning_session', 'UserLearningSession')
    SessionStatistics = apps.get_model('learning_session', 'LearningSessionStatistics')
    sessions_without_statistics = Session.objects.filter(statistics=None)
    new_statistics = []
    for session in sessions_without_statistics:
        new_statistics.append(SessionStatistics(session=session))
    SessionStatistics.objects.bulk_create(new_statistics, batch_size=5000)


class Migration(migrations.Migration):

    dependencies = [
        ('learning_session', '0005_remove_userlearningsession_average_rating_and_more'),
    ]

    operations = [
        migrations.RunPython(create_learning_session_statistics)
    ]
