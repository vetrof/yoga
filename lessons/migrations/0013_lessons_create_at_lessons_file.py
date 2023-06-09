# Generated by Django 4.1.7 on 2023-04-06 12:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0012_lessons_video_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessons',
            name='create_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='lessons',
            name='file',
            field=models.FileField(default='--', upload_to='video/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['mp4'])]),
        ),
    ]
