# Generated by Django 4.1.7 on 2023-03-31 08:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lessons', '0003_lessons_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lessons',
            name='tags',
        ),
    ]
