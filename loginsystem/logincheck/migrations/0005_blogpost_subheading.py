# Generated by Django 3.0.8 on 2020-08-09 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logincheck', '0004_auto_20200809_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='subheading',
            field=models.TextField(default='subheading', max_length=100),
            preserve_default=False,
        ),
    ]