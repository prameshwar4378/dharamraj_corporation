# Generated by Django 4.2.1 on 2023-12-31 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Developer', '0020_alter_account_transaction_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='transaction_date',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='purchase_date',
            field=models.DateTimeField(auto_now_add=True, db_index=True),
        ),
    ]
