# Generated by Django 4.2.1 on 2023-06-03 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_module', '0002_auto_20220220_1836'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='عنوان')),
                ('url', models.CharField(max_length=200, verbose_name='لینک')),
                ('url_title', models.CharField(max_length=200, verbose_name='عنوان لینک')),
                ('description', models.TextField(verbose_name='توضیحات اسلایدر')),
                ('image', models.ImageField(upload_to='images/slider/', verbose_name='تصویر اسلایدر')),
            ],
            options={
                'verbose_name': 'اسلایدر',
                'verbose_name_plural': 'اسلایدر ها',
            },
        ),
    ]
