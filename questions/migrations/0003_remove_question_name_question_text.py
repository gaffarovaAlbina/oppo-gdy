# Generated by Django 4.0.4 on 2022-05-03 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='name',
        ),
        migrations.AddField(
            model_name='question',
            name='text',
            field=models.TextField(default=''),
        ),
    ]
