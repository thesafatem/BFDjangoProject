# Generated by Django 3.1.7 on 2021-05-12 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_tournamentbasemodel_questions_per_tour'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournamentbasemodel',
            name='deleted',
            field=models.BooleanField(default=False),
        ),
    ]
