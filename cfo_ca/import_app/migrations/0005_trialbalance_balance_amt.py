# Generated by Django 2.2 on 2021-02-23 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('import_app', '0004_auto_20210223_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='trialbalance',
            name='balance_amt',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=20, null=True),
        ),
    ]