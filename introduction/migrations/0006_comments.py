# Generated by Django 3.0.6 on 2021-04-17 08:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("introduction", "0005_auto_20210415_1748"),
    ]

    operations = [
        migrations.CreateModel(
            name="comments",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=200)),
                ("comment", models.CharField(max_length=400)),
            ],
        ),
    ]
