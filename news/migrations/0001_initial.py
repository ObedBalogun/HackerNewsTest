# Generated by Django 4.1.1 on 2022-09-19 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_id', models.IntegerField(unique=True)),
                ('title', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('news', 'News'), ('article', 'Article')], max_length=10)),
                ('score', models.IntegerField(default=0)),
                ('url', models.URLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
