# Generated by Django 4.0.1 on 2022-03-08 10:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0004_alter_productdb_weight'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productdb',
            name='weight',
            field=models.CharField(blank=True, max_length=100, null=True, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')]),
        ),
    ]
