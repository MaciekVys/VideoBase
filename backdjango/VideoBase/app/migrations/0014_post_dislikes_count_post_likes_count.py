# Generated by Django 5.0.3 on 2024-04-16 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_post_expiration_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='dislikes_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='likes_count',
            field=models.IntegerField(default=0),
        ),
    ]