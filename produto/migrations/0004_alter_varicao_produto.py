# Generated by Django 4.1.1 on 2022-09-30 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("produto", "0003_alter_varicao_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="varicao",
            name="produto",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="produto.produto",
                verbose_name="Excluir",
            ),
        ),
    ]