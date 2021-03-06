# Generated by Django 2.2.7 on 2020-01-04 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BankNames',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bank_name', models.CharField(max_length=100)),
                ('image_url', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='CurrencyRates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sell_USD', models.FloatField()),
                ('buy_USD', models.FloatField()),
                ('sell_EUR', models.FloatField()),
                ('buy_EUR', models.FloatField()),
            ],
        ),
    ]
