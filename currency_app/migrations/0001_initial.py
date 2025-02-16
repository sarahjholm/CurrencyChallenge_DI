# Generated by Django 5.0.6 on 2024-06-26 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CurrencyRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(unique=True)),
                ('value', models.FloatField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='RequestedRates',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('end_date', models.DateTimeField()),
                ('value', models.FloatField(max_length=6)),
            ],
        ),
    ]
