# Generated by Django 4.0.1 on 2022-03-25 09:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Userviewapp', '0007_checkout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checkout',
            name='userid',
        ),
    ]
