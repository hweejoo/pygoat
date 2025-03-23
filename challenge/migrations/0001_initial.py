# Generated by Django 4.0.4 on 2023-03-03 06:33

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Challenge",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("name", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("docker_image", models.CharField(max_length=100)),
                ("start_port", models.IntegerField()),
                ("end_port", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("flag", models.CharField(max_length=100)),
                ("point", models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name="UserChallenge",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("container_id", models.CharField(max_length=100)),
                ("port", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_live", models.BooleanField(default=False)),
                ("no_of_attempt", models.IntegerField(default=0)),
                ("is_solved", models.BooleanField(default=False)),
                (
                    "challenge",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="challenge.challenge",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
