# Generated by Django 4.0.3 on 2022-03-16 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0002_alter_evento_data_evento'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='evento',
            name='data_evento',
        ),
    ]
