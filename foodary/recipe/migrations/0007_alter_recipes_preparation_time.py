# Generated by Django 4.2.1 on 2023-05-08 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0006_alter_ingredients_options_alter_instructions_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipes',
            name='preparation_time',
            field=models.IntegerField(help_text='duration in minutes'),
        ),
    ]