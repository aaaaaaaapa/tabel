# Generated by Django 5.1.4 on 2024-12-17 11:11

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tabel', '0002_alter_employeeaccounting_employment_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeaccounting',
            name='employment_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата приема'),
        ),
        migrations.AlterField(
            model_name='tabel',
            name='date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата'),
        ),
        migrations.AlterField(
            model_name='vacation',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='Дата начала'),
        ),
    ]
