# Generated by Django 4.0 on 2022-03-08 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('launchpad', '0005_hostedcollection_premint'),
    ]

    operations = [
        migrations.AddField(
            model_name='hostedcollection',
            name='metadata_generated',
            field=models.BooleanField(default=False),
        ),
    ]