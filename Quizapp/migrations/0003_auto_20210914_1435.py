# Generated by Django 3.2.7 on 2021-09-14 14:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('Quizapp', '0002_auto_20210914_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answers',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('77149a1a-088c-4caf-9f92-d87d2ba941e1'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='categories',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('77149a1a-088c-4caf-9f92-d87d2ba941e1'), primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='questions',
            name='uid',
            field=models.UUIDField(default=uuid.UUID('77149a1a-088c-4caf-9f92-d87d2ba941e1'), primary_key=True, serialize=False),
        ),
    ]
