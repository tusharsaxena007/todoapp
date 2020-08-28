# Generated by Django 3.0.8 on 2020-08-12 10:34

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('logincheck', '0007_auto_20200812_1550'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='dislike',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='dislike',
            field=models.ManyToManyField(related_name='dislikes', to=settings.AUTH_USER_MODEL),
        ),
    ]
