# Generated by Django 4.2 on 2023-04-21 08:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='bestseller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.PositiveBigIntegerField()),
                ('discription', models.TextField()),
                ('category', models.CharField(choices=[('TO', 'Top'), ('SK', 'Skirt'), ('PA', 'Pants'), ('SH', 'Shorts')], max_length=2)),
                ('size', models.CharField(choices=[('Xs', 'Xs'), ('S', 'S'), ('M', 'M'), ('L', 'L')], max_length=2)),
                ('color', models.CharField(choices=[('black', 'black'), ('navy', 'navy'), ('gray', 'gray'), ('yellow', 'yellow'), ('LB', 'light blue'), ('red', 'red'), ('white', 'white')], max_length=10)),
                ('product_image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('mobile', models.IntegerField(default=0)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(max_length=30)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.PositiveIntegerField()),
                ('discription', models.TextField()),
                ('category', models.CharField(choices=[('TO', 'Top'), ('SK', 'Skirt'), ('PA', 'Pants'), ('SH', 'Shorts')], max_length=2)),
                ('size', models.CharField(choices=[('Xs', 'Xs'), ('S', 'S'), ('M', 'M'), ('L', 'L')], max_length=2)),
                ('color', models.CharField(choices=[('black', 'black'), ('navy', 'navy'), ('gray', 'gray'), ('yellow', 'yellow'), ('LB', 'light blue'), ('red', 'red'), ('white', 'white')], max_length=10)),
                ('product_image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Top',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.PositiveBigIntegerField()),
                ('discription', models.TextField()),
                ('category', models.CharField(choices=[('TO', 'Top'), ('SK', 'Skirt'), ('PA', 'Pants'), ('SH', 'Shorts')], max_length=2)),
                ('size', models.CharField(choices=[('Xs', 'Xs'), ('S', 'S'), ('M', 'M'), ('L', 'L')], max_length=2)),
                ('color', models.CharField(choices=[('black', 'black'), ('navy', 'navy'), ('gray', 'gray'), ('yellow', 'yellow'), ('LB', 'light blue'), ('red', 'red'), ('white', 'white')], max_length=10)),
                ('product_image', models.ImageField(upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField()),
                ('rezorpay_order_id', models.CharField(blank=True, max_length=100, null=True)),
                ('rezorpay_payment_status', models.CharField(blank=True, max_length=100, null=True)),
                ('rezorpay_payment_id', models.CharField(blank=True, max_length=100, null=True)),
                ('paid', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On the way', 'On the way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel'), ('Pending', 'Pending')], default='Pending', max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
