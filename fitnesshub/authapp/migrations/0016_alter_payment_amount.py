# Generated by Django 5.0.2 on 2024-03-31 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0015_remove_payment_equipment_remove_payment_method_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]
