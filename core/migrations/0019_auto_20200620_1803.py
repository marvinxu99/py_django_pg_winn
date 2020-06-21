# Generated by Django 3.0.7 on 2020-06-21 01:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_auto_20200620_1801'),
    ]

    operations = [
        migrations.RemoveIndex(
            model_name='itembarcode',
            name='core_itemba_item_id_5211a8_idx',
        ),
        migrations.RemoveIndex(
            model_name='itembarcode',
            name='core_itemba_value_655a10_idx',
        ),
        migrations.RemoveIndex(
            model_name='itemidentifier',
            name='core_itemid_item_id_a34980_idx',
        ),
        migrations.RemoveIndex(
            model_name='itempricehist',
            name='core_itempr_item_id_9826a8_idx',
        ),
        migrations.RemoveIndex(
            model_name='itempricehist',
            name='core_itempr_item_pr_6f68ed_idx',
        ),
        migrations.RemoveIndex(
            model_name='itempricehist',
            name='core_itempr_contrac_da1781_idx',
        ),
        migrations.RemoveIndex(
            model_name='itempricehist',
            name='core_itempr_organiz_eb5695_idx',
        ),
        migrations.RemoveIndex(
            model_name='itempricehist',
            name='core_itempr_package_6eca66_idx',
        ),
        migrations.AddIndex(
            model_name='itembarcode',
            index=models.Index(fields=['item'], name='core_item_b_item_id_ad1058_idx'),
        ),
        migrations.AddIndex(
            model_name='itembarcode',
            index=models.Index(fields=['value'], name='core_item_b_value_c1777c_idx'),
        ),
        migrations.AddIndex(
            model_name='itemidentifier',
            index=models.Index(fields=['item'], name='core_item_i_item_id_dbec6f_idx'),
        ),
        migrations.AddIndex(
            model_name='itempricehist',
            index=models.Index(fields=['item'], name='core_item_p_item_id_ffb9fa_idx'),
        ),
        migrations.AddIndex(
            model_name='itempricehist',
            index=models.Index(fields=['item_price'], name='core_item_p_item_pr_327362_idx'),
        ),
        migrations.AddIndex(
            model_name='itempricehist',
            index=models.Index(fields=['contract_line_id'], name='core_item_p_contrac_8fff96_idx'),
        ),
        migrations.AddIndex(
            model_name='itempricehist',
            index=models.Index(fields=['organization_id'], name='core_item_p_organiz_b133a3_idx'),
        ),
        migrations.AddIndex(
            model_name='itempricehist',
            index=models.Index(fields=['package_type_id'], name='core_item_p_package_24d846_idx'),
        ),
        migrations.AlterModelTable(
            name='itembarcode',
            table='core_item_barcode',
        ),
        migrations.AlterModelTable(
            name='itemidentifier',
            table='core_item_identifier',
        ),
        migrations.AlterModelTable(
            name='itempricehist',
            table='core_item_price_hist',
        ),
    ]
