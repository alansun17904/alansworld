# Generated by Django 2.1.1 on 2019-06-30 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('thoughtwall', '0008_auto_20190625_1659'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ('-published_date',)},
        ),
    ]
