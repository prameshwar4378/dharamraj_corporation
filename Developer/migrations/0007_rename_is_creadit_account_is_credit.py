# Generated by Django 4.2.1 on 2023-12-03 15:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Developer', '0006_account_is_creadit_account_is_debit'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='is_creadit',
            new_name='is_credit',
        ),
    ]
