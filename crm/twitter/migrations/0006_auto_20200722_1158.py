# Generated by Django 2.2 on 2020-07-22 06:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0005_auto_20200722_1106'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
