# Generated by Django 4.0.1 on 2022-02-08 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0011_alter_tag_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Applied',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.TextField(unique=True)),
            ],
        ),
    ]