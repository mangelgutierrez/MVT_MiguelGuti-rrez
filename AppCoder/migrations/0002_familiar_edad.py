# Generated by Django 4.1 on 2022-08-29 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiar',
            name='edad',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
