# Generated by Django 4.2.1 on 2023-12-09 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Developer', '0016_performainvoiceitem_gst_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='performainvoiceitem',
            name='total_amount',
            field=models.IntegerField(null=True),
        ),
    ]
