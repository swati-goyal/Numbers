# Generated by Django 2.0a1 on 2017-12-26 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tellifprime', '0003_auto_20171226_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numvalue',
            name='number_value',
            field=models.IntegerField(default=0),
        ),
    ]
