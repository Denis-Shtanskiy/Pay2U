# Generated by Django 3.2.3 on 2024-04-03 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0003_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tariffkind',
            options={'ordering': ('-cost_per_month',), 'verbose_name': 'Тариф', 'verbose_name_plural': 'Тарифы'},
        ),
    ]
