# Generated by Django 2.1.1 on 2018-10-20 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musicstoreadmin', '0005_auto_20181020_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='base_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
