# Generated by Django 4.2.1 on 2023-12-03 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Developer', '0005_rename_transaction_method_account_payment_mode_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='is_creadit',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='account',
            name='is_debit',
            field=models.BooleanField(default=False),
        ),
    ]
