# Generated by Django 5.1.5 on 2025-02-01 18:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('e_networks', '0008_product_count_product_created_at_product_price_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='network_node',
        ),
    ]
