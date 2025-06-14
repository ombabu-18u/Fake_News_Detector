# Generated by Django 4.2.21 on 2025-05-13 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detector', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsarticle',
            name='credibility_score',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='keywords',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='newsarticle',
            name='source_reliability',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
