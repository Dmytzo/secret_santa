# Generated by Django 2.1.4 on 2018-12-27 20:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hohoho', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='game',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='players', to='hohoho.SecretSanta'),
        ),
    ]