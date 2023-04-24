# Generated by Django 4.2 on 2023-04-21 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_rename_posts_post"),
    ]

    operations = [
        migrations.CreateModel(
            name="LikePost",
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
                ("post_id", models.CharField(max_length=500)),
                ("username", models.CharField(max_length=100)),
            ],
        ),
    ]
