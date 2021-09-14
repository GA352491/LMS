# Generated by Django 3.2.7 on 2021-09-14 14:16

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('uid', models.UUIDField(default=uuid.UUID('73d04e63-58c0-492d-92ee-a67bf317e04d'), primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('uid', models.UUIDField(default=uuid.UUID('73d04e63-58c0-492d-92ee-a67bf317e04d'), primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('question', models.CharField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='category_questions', to='Quizapp.categories')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('uid', models.UUIDField(default=uuid.UUID('73d04e63-58c0-492d-92ee-a67bf317e04d'), primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('answer', models.CharField(max_length=100)),
                ('is_correct', models.BooleanField(default=False)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_ans', to='Quizapp.questions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
