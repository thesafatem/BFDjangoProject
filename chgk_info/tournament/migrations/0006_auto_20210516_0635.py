# Generated by Django 3.1.7 on 2021-05-16 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0001_initial'),
        ('tournament', '0005_auto_20210516_0559'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tournamentcompetitorsplayers',
            name='player',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tournaments', to='player.player'),
        ),
    ]