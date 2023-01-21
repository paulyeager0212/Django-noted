# Generated by Django 4.1.3 on 2023-01-17 19:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("actions", "0002_alter_action_verb"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="action",
            name="user",
        ),
        migrations.AddField(
            model_name="action",
            name="actor_ct",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="actor_obj",
                to="contenttypes.contenttype",
            ),
        ),
        migrations.AddField(
            model_name="action",
            name="actor_id",
            field=models.PositiveIntegerField(blank=True, db_index=True, null=True),
        ),
        migrations.AlterField(
            model_name="action",
            name="verb",
            field=models.CharField(
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
    ]
