# Generated by Django 3.0.7 on 2020-06-26 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medium_api', '0002_article_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='claps',
            field=models.IntegerField(default=0),
        ),
    ]
