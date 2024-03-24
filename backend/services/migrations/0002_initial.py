# Generated by Django 3.2.3 on 2024-03-24 20:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subscriptions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='service',
            name='category',
            field=models.ForeignKey(blank=True, max_length=30, null=True, on_delete=django.db.models.deletion.SET_NULL, to='services.category', verbose_name='категория'),
        ),
        migrations.AddConstraint(
            model_name='subscription',
            constraint=models.UniqueConstraint(fields=('user', 'service'), name='unique_subscription'),
        ),
    ]
