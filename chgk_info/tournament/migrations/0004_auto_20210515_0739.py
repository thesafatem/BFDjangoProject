# Generated by Django 3.1.7 on 2021-05-15 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tournament', '0003_auto_20210515_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournamentcompetitorsplayers',
            name='tournament_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='players', to='tournament.tournamentcompetitorsteams'),
        ),
    ]
