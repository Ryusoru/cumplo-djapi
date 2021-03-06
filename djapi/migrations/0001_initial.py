# Generated by Django 2.1.1 on 2018-09-21 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('uf_indicator', models.BooleanField(default=False)),
                ('dolar_indicator', models.BooleanField(default=False)),
                ('tmc_indicator', models.BooleanField(default=False)),
            ],
        ),
    ]
