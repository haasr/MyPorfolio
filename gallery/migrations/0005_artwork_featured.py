# Generated by Django 4.2.3 on 2023-07-12 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0004_alter_artwork_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='artwork',
            name='featured',
            field=models.BooleanField(default=False, help_text='Feature this artwork on the home page'),
            preserve_default=False,
        ),
    ]
