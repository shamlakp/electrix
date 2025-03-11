# Generated by Django 5.0.1 on 2025-03-09 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_admin_product_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='created_at',
        ),
        migrations.AddField(
            model_name='product',
            name='categoryimage',
            field=models.ImageField(default='category_images/default.jpg', upload_to='category_images/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='product_images/default.jpg', upload_to='product_images/'),
        ),
    ]
