# Generated by Django 2.0a1 on 2017-12-26 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NumValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_value', models.IntegerField()),
                ('number_property', models.CharField(default='Try another number!', max_length=270,
                                                     verbose_name='properties')),
            ],
        ),
    ]