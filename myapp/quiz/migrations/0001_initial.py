# Generated by Django 5.1.4 on 2024-12-17 21:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Question",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("QuesText", models.CharField(max_length=255)),
                ("OptionA", models.CharField(max_length=100)),
                ("OptionB", models.CharField(max_length=100)),
                ("OptionC", models.CharField(max_length=100)),
                ("OptionD", models.CharField(max_length=100)),
                ("OptionAns", models.CharField(max_length=1)),
            ],
            options={
                "db_table": "quiz_question",
            },
        ),
    ]