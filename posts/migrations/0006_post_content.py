# Generated by Django 4.1.7 on 2023-03-01 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0005_remove_post_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="content",
            field=models.TextField(default=None),
        ),
    ]
