# Generated by Django 2.1.1 on 2018-10-21 02:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('musicstoreadmin', '0006_auto_20181020_1739'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='delivery_fee',
        ),
        migrations.RemoveField(
            model_name='order',
            name='total_price',
        ),
    ]