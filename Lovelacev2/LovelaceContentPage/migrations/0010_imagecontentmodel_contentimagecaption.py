# Generated by Django 3.1.1 on 2021-03-22 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('LovelaceContentPage', '0009_auto_20210322_1436'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagecontentmodel',
            name='ContentImageCaption',
            field=models.CharField(default='Caption', max_length=100),
            preserve_default=False,
        ),
    ]
