# Generated by Django 2.0.7 on 2018-07-11 12:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('firstapp', '0002_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='people',
            name='email',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='people',
            name='phone',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='people',
            name='pwd',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
