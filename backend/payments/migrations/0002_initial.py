# Generated by Django 3.2.3 on 2024-04-04 18:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tariffkind',
            name='service',
            field=models.ManyToManyField(related_name='tariffs_services', to='services.Service', verbose_name='Сервис'),
        ),
        migrations.AddField(
            model_name='payment',
            name='service',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_services', to='services.service', verbose_name='Сервис'),
        ),
        migrations.AddField(
            model_name='payment',
            name='subscription',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_subscriptions', to='services.subscription', verbose_name='Подписка'),
        ),
        migrations.AddField(
            model_name='payment',
            name='tariff_kind',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_tariffs', to='payments.tariffkind', verbose_name='Выбранный тариф'),
        ),
    ]
