# Generated by Django 2.2.2 on 2019-06-18 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thoughtwall', '0002_question_published_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='published_date',
            field=models.DateTimeField(),
        ),
    ]
