# Generated by Django 2.2.2 on 2019-06-18 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thoughtwall', '0003_auto_20190619_0022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='answer_text',
            field=models.CharField(max_length=20000, null=True),
        ),
    ]