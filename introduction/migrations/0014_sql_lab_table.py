# Generated by Django 4.0.3 on 2022-04-23 09:41

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "introduction",
            "0013_alter_comments_id_alter_faang_id_alter_info_id_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="sql_lab_table",
            fields=[
                (
                    "id",
                    models.CharField(max_length=200, primary_key=True, serialize=False),
                ),
                ("password", models.CharField(max_length=200)),
            ],
        ),
    ]
