# Generated by Django 4.2.5 on 2024-01-27 10:19

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_news_options_alter_user_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]