# Generated by Django 3.0.7 on 2020-06-21 00:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0016_auto_20200620_1732'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='itemprice',
            name='core_itempr_item_id_091a37_idx',
        ),
        migrations.RemoveIndex(
            model_name='itemprice',
            name='core_itempr_contrac_11f5b0_idx',
        ),
        migrations.AddIndex(
            model_name='itemprice',
            index=models.Index(fields=['item'], name='item_price_item_id_4d4cb0_idx'),
        ),
        migrations.AddIndex(
            model_name='itemprice',
            index=models.Index(fields=['contract_line_id'], name='item_price_contrac_17515c_idx'),
        ),
        migrations.AlterModelTable(
            name='itemprice',
            table='item_price',
        ),
    ]
