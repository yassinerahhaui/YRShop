# Generated by Django 3.2 on 2022-03-31 14:01

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
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('icon', models.ImageField(max_length=200, null=True, upload_to='')),
                ('image_header', models.ImageField(max_length=200, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Collection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(max_length=200, null=True, upload_to='')),
                ('description', models.TextField(blank=True, max_length=3000, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_collection', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('old_price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('description', models.TextField(blank=True, max_length=3000, null=True)),
                ('details', models.TextField(blank=True, max_length=3000, null=True)),
                ('image', models.ImageField(max_length=200, null=True, upload_to='')),
                ('image1', models.ImageField(blank=True, max_length=200, null=True, upload_to='')),
                ('image2', models.ImageField(blank=True, max_length=200, null=True, upload_to='')),
                ('image3', models.ImageField(blank=True, max_length=200, null=True, upload_to='')),
                ('image4', models.ImageField(blank=True, max_length=200, null=True, upload_to='')),
                ('image5', models.ImageField(blank=True, max_length=200, null=True, upload_to='')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('stock_out', models.BooleanField(default=False)),
                ('sale', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='product_category', to='Store.category')),
                ('collection', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='product_collection', to='Store.collection')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_product', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
