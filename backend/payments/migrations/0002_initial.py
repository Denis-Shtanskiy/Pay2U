# Generated by Django 3.2.3 on 2024-04-07 11:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('payments', '0001_initial'),
        ('services', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tariffkind',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tariffs_services', to='services.service', verbose_name='Сервис'),
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
