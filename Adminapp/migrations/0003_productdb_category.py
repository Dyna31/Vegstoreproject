# Generated by Django 4.0.1 on 2022-03-08 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Adminapp', '0002_productdb'),
    ]

    operations = [
        migrations.AddField(
            model_name='productdb',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
