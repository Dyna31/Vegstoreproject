# Generated by Django 4.0.1 on 2022-03-24 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Userviewapp', '0006_cartdb_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='checkout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100, null=True)),
                ('lastname', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
                ('streetaddress', models.CharField(max_length=100, null=True)),
                ('town', models.CharField(max_length=100, null=True)),
                ('postcode', models.IntegerField(null=True)),
                ('phone', models.IntegerField(null=True)),
                ('status', models.IntegerField(null=True)),
                ('cartid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Userviewapp.cartdb')),
                ('userid', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Userviewapp.regidb')),
            ],
        ),
    ]
