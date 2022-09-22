# Generated by Django 3.2.15 on 2022-09-22 15:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scip', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Naics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('naics_id', models.PositiveIntegerField()),
                ('description', models.CharField(max_length=255)),
                ('firms_total', models.PositiveIntegerField(null=True)),
                ('establishments_total', models.PositiveIntegerField(null=True)),
                ('industry_concentration', models.PositiveIntegerField(null=True)),
                ('domestic_mfg_capacity_per', models.PositiveIntegerField(null=True)),
                ('total_val_domestic_prod_per', models.PositiveIntegerField(null=True)),
                ('establishments_by_state', models.PositiveIntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='importing_firms',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='total_produced_domestic',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='total_value_exported',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='total_value_imported',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='industry',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.CreateModel(
            name='NaicsEstablishmentsState',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('establishments', models.PositiveIntegerField(null=True)),
                ('state', models.CharField(blank=True, max_length=255, null=True)),
                ('naics', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='scip.naics')),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='importing_firms_naics',
            field=models.ManyToManyField(null=True, related_name='importing_firms', to='scip.Naics'),
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturing_naics',
            field=models.ManyToManyField(null=True, related_name='manufacturing', to='scip.Naics'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_codes',
            field=models.ManyToManyField(null=True, related_name='product_codes', to='scip.ProductCode'),
        ),
    ]
