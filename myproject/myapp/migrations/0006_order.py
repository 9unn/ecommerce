# Generated by Django 4.2 on 2023-04-21 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_product_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_ids', models.PositiveBigIntegerField()),
                ('selling_price', models.PositiveBigIntegerField()),
            ],
        ),
    ]
