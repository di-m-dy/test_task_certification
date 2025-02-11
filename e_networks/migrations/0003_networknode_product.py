# Generated by Django 5.1.5 on 2025-01-29 13:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e_networks', '0002_contacts_google_map_link_alter_contacts_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkNode',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('debt', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Долг')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('contacts', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='e_networks.contacts', verbose_name='Контакты')),
                ('supplier', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='e_networks.networknode', verbose_name='Поставщик')),
            ],
            options={
                'verbose_name': 'звено сети',
                'verbose_name_plural': 'звенья сети',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Наименование')),
                ('model', models.CharField(blank=True, max_length=255, null=True, verbose_name='Модель')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Дата выхода продукта на рынок')),
                ('network_node', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='e_networks.networknode', verbose_name='Сетевое звено')),
            ],
            options={
                'verbose_name': 'продукт',
                'verbose_name_plural': 'продукты',
            },
        ),
    ]
