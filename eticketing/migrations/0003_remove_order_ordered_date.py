# Generated by Django 3.0.2 on 2020-01-25 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eticketing', '0002_order_ordered_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ordered_date',
        ),
    ]
