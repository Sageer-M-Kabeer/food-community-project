# Generated by Django 4.2.1 on 2023-05-08 03:16

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0004_recipes_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipes',
            name='ingredients',
        ),
        migrations.RemoveField(
            model_name='recipes',
            name='instructions',
        ),
        migrations.AddField(
            model_name='recipes',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Instructions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipes')),
            ],
            options={
                'verbose_name': 'instruction',
                'verbose_name_plural': 's',
            },
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255)),
                ('recipe', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipe.recipes')),
            ],
            options={
                'verbose_name': 'ingredient',
                'verbose_name_plural': 's',
            },
        ),
    ]
