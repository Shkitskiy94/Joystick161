# Generated by Django 4.1.4 on 2023-01-07 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image0',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Главное изображение'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image1',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Доп Изображение 1'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Доп Изображение 2'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image3',
            field=models.ImageField(blank=True, upload_to='images/', verbose_name='Доп Изображение 3'),
        ),
    ]
