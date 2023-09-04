# Generated by Django 4.1.3 on 2023-09-04 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('node', '0008_alter_nodemedia_type'),
        ('learning_session', '0019_nodelearningcontext_easiness'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nodelearningcontext',
            name='node',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='repetition_context', to='node.palacenode'),
        ),
    ]