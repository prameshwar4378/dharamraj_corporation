# Generated by Django 4.2.1 on 2023-11-27 05:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dealer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dealer_name', models.CharField(db_index=True, max_length=40)),
                ('business_name', models.CharField(db_index=True, max_length=40)),
                ('mobile_no', models.CharField(db_index=True, max_length=12)),
                ('email_id', models.CharField(db_index=True, max_length=40)),
                ('address', models.CharField(max_length=200)),
                ('pin_code', models.CharField(db_index=True, max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(db_index=True, max_length=50)),
                ('invoice_date', models.DateField(auto_now_add=True, db_index=True)),
                ('total_amount', models.IntegerField()),
                ('total_gst_amount', models.IntegerField()),
                ('dealer_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Developer.dealer')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_code', models.CharField(db_index=True, max_length=20, unique=True)),
                ('product_name', models.CharField(db_index=True, max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('sale_amount', models.IntegerField(null=True)),
                ('gst', models.CharField(choices=[('6', '6'), ('12', '12'), ('18', '18')], max_length=50, null=True)),
                ('available_stock', models.PositiveIntegerField(db_index=True, default=0)),
            ],
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_name', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('rate', models.IntegerField()),
                ('gst_percent', models.FloatField()),
                ('gst_amount', models.IntegerField()),
                ('total_amount', models.IntegerField()),
                ('grand_total', models.IntegerField()),
                ('Invoice', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Developer.invoice')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Developer.product')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('purchase_date', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Developer.product')),
            ],
        ),
        migrations.AddField(
            model_name='dealer',
            name='state',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Developer.state'),
        ),
    ]
