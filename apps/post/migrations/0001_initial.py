# Generated by Django 4.2.4 on 2023-08-31 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Fly",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                ("author", models.CharField(max_length=100)),
            ],
            options={
                "verbose_name_plural": "Flies",
            },
        ),
        migrations.CreateModel(
            name="FlyType",
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
                ("name", models.CharField(max_length=50)),
                ("description", models.TextField()),
            ],
            options={
                "verbose_name_plural": "Fly Types",
            },
        ),
        migrations.CreateModel(
            name="Post",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("modified_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=50)),
                ("body", models.TextField(blank=True, max_length=300, null=True)),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="PostType",
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
                ("type", models.CharField(max_length=50)),
                ("description", models.TextField()),
            ],
            options={
                "verbose_name_plural": "Post Types",
            },
        ),
        migrations.CreateModel(
            name="Tag",
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
                ("name", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="PostTag",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "post_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="post.post",
                        verbose_name="Post id",
                    ),
                ),
                (
                    "tag_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="post.tag",
                        verbose_name="Tag id",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "Post Types",
            },
        ),
        migrations.AddField(
            model_name="post",
            name="post_type_id",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="post.posttype",
                verbose_name="Post Type",
            ),
        ),
        migrations.AddField(
            model_name="post",
            name="tags",
            field=models.ManyToManyField(to="post.tag", verbose_name=""),
        ),
    ]
