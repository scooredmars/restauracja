# Generated by Django 2.2.8 on 2019-12-09 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("restaurant", "0004_auto_20191209_1238"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="categories",
            options={"verbose_name": "category", "verbose_name_plural": "categories"},
        ),
        migrations.AlterModelOptions(
            name="menu",
            options={"verbose_name": "menu", "verbose_name_plural": "menus"},
        ),
        migrations.AddField(
            model_name="menu",
            name="category",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="restaurant.Categories",
                verbose_name="Kategoria",
            ),
            preserve_default=False,
        ),
    ]
