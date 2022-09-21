# Generated by Django 4.1.1 on 2022-09-20 22:33

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_newsitem_text_alter_newsitem_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsitem',
            name='kids',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(default=0), blank=True, default=list, null=True, size=None),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='type',
            field=models.CharField(choices=[('news', 'News'), ('story', 'Story'), ('comment', 'Comment')], max_length=10),
        ),
    ]
