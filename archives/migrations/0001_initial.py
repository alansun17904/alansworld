# Generated by Django 2.2.2 on 2019-06-23 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PsychologyStudy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('BIO', 'Biological'), ('COG', 'Cognitive'), ('SC', 'Social Cultural')], default='BIO', max_length=3)),
                ('experimenters', models.CharField(max_length=200)),
                ('year', models.IntegerField()),
                ('aim', models.TextField()),
                ('method', models.CharField(max_length=500)),
                ('participants', models.TextField()),
                ('procedure', models.TextField()),
                ('results', models.TextField()),
                ('conclusion', models.TextField()),
                ('evaluation', models.TextField()),
                ('validquestions', models.TextField(null=True)),
            ],
        ),
    ]
