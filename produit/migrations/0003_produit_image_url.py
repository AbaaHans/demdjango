# Generated by Django 3.1.5 on 2021-02-11 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produit', '0002_auto_20210201_1504'),
    ]

    operations = [
        migrations.AddField(
            model_name='produit',
            name='image_url',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
