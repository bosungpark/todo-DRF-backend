# Generated by Django 4.0.1 on 2022-02-09 01:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0018_alter_tag_background_color_alter_tag_text_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='background_color',
            field=models.CharField(default='red', max_length=100),
        ),
        migrations.AlterField(
            model_name='tag',
            name='blog',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='tag',
            name='text_color',
            field=models.CharField(default='green', max_length=100),
        ),
    ]
