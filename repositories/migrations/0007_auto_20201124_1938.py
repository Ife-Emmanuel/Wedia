# Generated by Django 3.1.1 on 2020-11-24 18:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('repositories', '0006_auto_20201124_1935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='repository',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
