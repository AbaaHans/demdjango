# Generated by Django 3.1.5 on 2021-02-01 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='email',
            field=models.CharField(max_length=200, null=True),
        ),
    ]