# Generated by Django 3.1.1 on 2021-03-17 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LectureContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Parent', models.CharField(max_length=100)),
                ('Index', models.PositiveIntegerField(max_length=100)),
                ('ContentType', models.CharField(max_length=100)),
                ('ContentText', models.CharField(max_length=500)),
            ],
        ),
    ]
