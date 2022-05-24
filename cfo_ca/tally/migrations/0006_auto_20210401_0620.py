# Generated by Django 2.2 on 2021-04-01 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tally', '0005_auto_20210325_0148'),
    ]

    operations = [
        migrations.AddField(
            model_name='customgroup',
            name='group_type',
            field=models.CharField(blank=True, choices=[('BS', 'Balance Sheet'), ('P&L', 'Profit & Loss')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='group',
            name='group_type',
            field=models.CharField(blank=True, choices=[('BS', 'Balance Sheet'), ('P&L', 'Profit & Loss')], max_length=20, null=True),
        ),
    ]
