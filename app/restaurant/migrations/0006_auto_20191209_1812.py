# Generated by Django 2.2.8 on 2019-12-09 17:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0005_auto_20191209_1242'),
    ]

    operations = [
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='gallery', verbose_name='Gallery image')),
            ],
            options={
                'verbose_name': 'image',
                'verbose_name_plural': 'images',
            },
        ),
        migrations.AlterField(
            model_name='categories',
            name='image',
            field=models.ImageField(upload_to='', verbose_name='Menu background'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='name',
            field=models.CharField(max_length=70, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='thumbnail',
            field=models.ImageField(upload_to='', verbose_name='Home thumbnail'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='restaurant.Categories', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='description',
            field=models.TextField(max_length=500, verbose_name='Ingredients'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='dish',
            field=models.TextField(max_length=150, verbose_name='Dish name'),
        ),
    ]
