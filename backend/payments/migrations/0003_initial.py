# Generated by Django 3.2.3 on 2024-04-04 18:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('payments', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_users', to=settings.AUTH_USER_MODEL, verbose_name='Плательщик'),
        ),
        migrations.AddField(
            model_name='cashback',
            name='payment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='cashbacks', to='payments.payment', verbose_name='Платеж'),
        ),
    ]
