# Generated by Django 4.2.1 on 2023-12-09 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Developer', '0014_alter_invoice_invoice_number_performainvoice'),
    ]

    operations = [
        migrations.CreateModel(
            name='PerformaInvoiceItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('rate', models.IntegerField()),
                ('gst_percent', models.FloatField()),
                ('taxable_amount', models.IntegerField()),
                ('performa_invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Developer.performainvoice')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Developer.product')),
            ],
        ),
    ]
