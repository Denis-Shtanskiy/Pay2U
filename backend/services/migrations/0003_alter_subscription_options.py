# Generated by Django 3.2.3 on 2024-04-02 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='subscription',
            options={'verbose_name': 'Подписка', 'verbose_name_plural': 'Подписки'},
        ),
    ]
