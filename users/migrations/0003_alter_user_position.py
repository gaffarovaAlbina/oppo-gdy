# Generated by Django 4.0.4 on 2022-05-05 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_patronymic_user_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='position',
            field=models.CharField(default='', max_length=80),
        ),
    ]
