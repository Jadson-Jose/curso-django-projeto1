# Generated by Django 5.1.3 on 2024-11-29 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_alter_recipe_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cover',
            field=models.ImageField(blank=True, upload_to='recipes/covers/%Y/%m/%d'),
        ),
    ]