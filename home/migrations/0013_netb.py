# Generated by Django 4.1.13 on 2024-02-06 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_remove_upi_userid_upi_name_alter_upi_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='Netb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('number', models.EmailField(max_length=254)),
            ],
        ),
    ]
