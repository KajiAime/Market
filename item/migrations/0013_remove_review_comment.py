# Generated by Django 4.2.4 on 2023-10-08 10:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0012_remove_review_rating_review_rate_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='comment',
        ),
    ]
