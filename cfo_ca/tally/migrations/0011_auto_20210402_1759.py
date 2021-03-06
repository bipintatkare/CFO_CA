# Generated by Django 2.2 on 2021-04-02 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tally', '0010_auto_20210401_1708'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customgroup',
            name='balance_sheet_type',
            field=models.CharField(blank=True, choices=[('Assets', 'Assets'), ('Liabilities', 'Liabilities'), ('Expense', 'Expense'), ('Income', 'Income')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='balance_sheet_type',
            field=models.CharField(blank=True, choices=[('Assets', 'Assets'), ('Liabilities', 'Liabilities'), ('Expense', 'Expense'), ('Income', 'Income')], max_length=20, null=True),
        ),
    ]
