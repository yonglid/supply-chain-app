# Generated by Django 3.2.15 on 2022-11-03 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scip', '0005_auto_20221103_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='foreigntrade',
            name='year',
            field=models.CharField(default='', max_length=255),
        ),
    ]