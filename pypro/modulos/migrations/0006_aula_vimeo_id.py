# Generated by Django 3.1.7 on 2021-02-23 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0005_aula'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='vimeo_id',
            field=models.CharField(default='0', max_length=32),
        ),
    ]
