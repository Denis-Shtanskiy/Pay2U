# Generated by Django 3.2.3 on 2024-04-05 17:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_auto_20240405_0139'),
        ('payments', '0003_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tariffkind',
            name='service',
        ),
        migrations.AddField(
            model_name='tariffkind',
            name='service',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tariffs_services', to='services.service', verbose_name='Сервис'),
        ),
    ]