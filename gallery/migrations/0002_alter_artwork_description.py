# Generated by Django 4.2.3 on 2023-07-12 00:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artwork',
            name='description',
            field=models.TextField(default=''),
        ),
    ]
