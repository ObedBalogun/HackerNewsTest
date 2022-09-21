# Generated by Django 4.1.1 on 2022-09-21 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='from_api',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='newsitem',
            name='time_posted',
            field=models.IntegerField(default=0),
        ),
    ]
