# Generated by Django 3.1.1 on 2021-03-27 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LovelaceContentPage', '0011_filecontentmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filecontentmodel',
            name='ContentFile',
            field=models.CharField(max_length=100),
        ),
    ]
