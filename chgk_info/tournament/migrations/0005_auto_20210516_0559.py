# Generated by Django 3.1.7 on 2021-05-15 23:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
        ('tournament', '0004_auto_20210515_0739'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournamentcompetitorsplayers',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tournament', to='player.player'),
        ),
    ]
