# Generated by Django 4.2 on 2023-04-21 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_new'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bestseller',
            name='color',
            field=models.CharField(choices=[('black', 'black'), ('navy', 'navy'), ('gray', 'gray'), ('yellow', 'yellow'), ('LB', 'light blue'), ('red', 'red'), ('white', 'white'), ('blue', 'blue')], max_length=10),
        ),
        migrations.AlterField(
            model_name='new',
            name='color',
            field=models.CharField(choices=[('black', 'black'), ('navy', 'navy'), ('gray', 'gray'), ('yellow', 'yellow'), ('LB', 'light blue'), ('red', 'red'), ('white', 'white'), ('blue', 'blue')], max_length=10),
        ),
        migrations.AlterField(
            model_name='product',
            name='color',
            field=models.CharField(choices=[('black', 'black'), ('navy', 'navy'), ('gray', 'gray'), ('yellow', 'yellow'), ('LB', 'light blue'), ('red', 'red'), ('white', 'white'), ('blue', 'blue')], max_length=10),
        ),
        migrations.AlterField(
            model_name='top',
            name='color',
            field=models.CharField(choices=[('black', 'black'), ('navy', 'navy'), ('gray', 'gray'), ('yellow', 'yellow'), ('LB', 'light blue'), ('red', 'red'), ('white', 'white'), ('blue', 'blue')], max_length=10),
        ),
    ]
