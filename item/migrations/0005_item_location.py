# Generated by Django 4.2.4 on 2023-09-22 15:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0004_item_is_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='location',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
        ),
    ]
