# Generated by Django 4.1.7 on 2023-03-01 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0003_remove_postimage_paragraph_postimage_post"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="postparagraph",
            name="post",
        ),
        migrations.AddField(
            model_name="post",
            name="content",
            field=models.TextField(default=None),
        ),
        migrations.DeleteModel(
            name="PostImage",
        ),
        migrations.DeleteModel(
            name="PostParagraph",
        ),
    ]
