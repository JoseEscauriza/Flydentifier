# Generated by Django 4.2.4 on 2023-09-09 13:22

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("post", "0003_alter_posttag_options_fly_mat_amount_fly_upload_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="upload",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="post_img_dir",
                verbose_name="Image upload",
            ),
        ),
        migrations.AlterField(
            model_name="fly",
            name="upload",
            field=models.ImageField(
                blank=True,
                null=True,
                upload_to="fly_img_dir",
                verbose_name="Image upload",
            ),
        ),
    ]
