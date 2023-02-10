# Generated by Django 4.1.3 on 2023-02-08 13:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
    ]

    operations = [
        migrations.CreateModel(
            name="Action",
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
                (
                    "actor_id",
                    models.PositiveIntegerField(blank=True, db_index=True, null=True),
                ),
                (
                    "verb",
                    models.CharField(
                        choices=[
                            ("new", "new"),
                            ("creates", "creates"),
                            ("follows", "follows"),
                            ("bookmarks", "bookmarks"),
                            ("likes", "likes"),
                            ("downloads", "downloads"),
                        ],
                        max_length=255,
                    ),
                ),
                ("created", models.DateField(auto_now_add=True, db_index=True)),
                (
                    "target_id",
                    models.PositiveIntegerField(blank=True, db_index=True, null=True),
                ),
                (
                    "actor_ct",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="actor_obj",
                        to="contenttypes.contenttype",
                    ),
                ),
                (
                    "target_ct",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="target_obj",
                        to="contenttypes.contenttype",
                    ),
                ),
            ],
            options={
                "ordering": ("-created",),
            },
        ),
    ]
