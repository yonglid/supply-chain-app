# Generated by Django 3.2.15 on 2022-11-23 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scip', '0009_auto_20221123_1723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productcode',
            old_name='description',
            new_name='active_description',
        ),
        migrations.AddField(
            model_name='productcode',
            name='desc2_4',
            field=models.TextField(default='', null=True),
        ),
        migrations.AddField(
            model_name='productcode',
            name='descript_L',
            field=models.TextField(default='', null=True),
        ),
    ]
