# Generated by Django 3.2.9 on 2021-11-23 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20211123_2141'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scopearticle',
            name='is_main',
            field=models.BooleanField(),
        ),
    ]
