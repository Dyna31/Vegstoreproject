# Generated by Django 4.0.1 on 2022-03-09 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userviewapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='contactdb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameu', models.CharField(max_length=100, null=True)),
                ('emailu', models.CharField(max_length=100, null=True)),
                ('subject', models.CharField(max_length=100, null=True)),
                ('message', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]