# Generated by Django 4.1.1 on 2022-09-19 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0006_alter_post_imagem_post"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="imagem_post",
            field=models.ImageField(
                blank=True, null=True, upload_to="media/post_img", verbose_name="Imagem"
            ),
        ),
    ]
