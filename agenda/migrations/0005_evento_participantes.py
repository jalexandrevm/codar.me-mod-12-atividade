# Generated by Django 4.0.3 on 2022-03-16 22:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0004_evento_data_evento'),
    ]

    operations = [
        migrations.AddField(
            model_name='evento',
            name='participantes',
            field=models.IntegerField(default=0),
        ),
    ]
