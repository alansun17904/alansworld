# Generated by Django 2.1.1 on 2019-06-30 02:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('archives', '0004_psychologystudy_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='psychologystudy',
            name='slug',
        ),
    ]
