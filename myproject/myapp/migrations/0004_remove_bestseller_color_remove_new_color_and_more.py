# Generated by Django 4.2 on 2023-04-21 10:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_bestseller_color_alter_new_color_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bestseller',
            name='color',
        ),
        migrations.RemoveField(
            model_name='new',
            name='color',
        ),
        migrations.RemoveField(
            model_name='product',
            name='color',
        ),
        migrations.RemoveField(
            model_name='top',
            name='color',
        ),
    ]
