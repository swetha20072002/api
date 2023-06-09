# Generated by Django 2.2.4 on 2019-08-11 13:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import mptt.fields
import products.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('icon', models.ImageField(upload_to=products.models.category_image_path)),
                ('lft', models.PositiveIntegerField(editable=False)),
                ('rght', models.PositiveIntegerField(editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(editable=False)),
                ('children', mptt.fields.TreeForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='parent', to='products.Category')),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=250)),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('image', models.ImageField(upload_to=products.models.product_image_path)),
                ('description', models.TextField(blank=True, null=True)),
                ('quantity', models.IntegerField()),
                ('views', models.IntegerField(default=0)),
                ('category', mptt.fields.TreeForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='product_category', to='products.Category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_product', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
