# Generated by Django 3.1.3 on 2020-11-23 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20201123_1652'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertie',
            name='latitude',
        ),
        migrations.RemoveField(
            model_name='propertie',
            name='longitude',
        ),
    ]