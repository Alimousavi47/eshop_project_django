# Generated by Django 4.2.1 on 2023-06-05 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account_module', '0002_auto_20220204_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about_user',
            field=models.TextField(blank=True, null=True, verbose_name='درباره شخص'),
        ),
    ]
