# Generated by Django 2.2 on 2020-07-24 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitterapp', '0002_auto_20200723_0534'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='mode',
            field=models.CharField(choices=[('public', 'Public'), ('private', 'Private')], default='public', max_length=50),
        ),
    ]
