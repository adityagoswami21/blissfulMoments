# Generated by Django 5.1.5 on 2025-04-17 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0005_order_date_shipped'),
    ]

    operations = [
        migrations.AddField(
            model_name='shippingaddress',
            name='shipping_email',
            field=models.CharField(default='noemail@example.com', max_length=255),
            preserve_default=False,
        ),
    ]
