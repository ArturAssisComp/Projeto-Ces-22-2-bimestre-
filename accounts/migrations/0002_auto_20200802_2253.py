# Generated by Django 3.0.8 on 2020-08-03 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='cidade',
            field=models.CharField(default='', max_length=50),
        ),
        migrations.AddField(
            model_name='profile',
            name='profissão',
            field=models.CharField(default='', max_length=50),
        ),
    ]