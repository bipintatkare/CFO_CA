# Generated by Django 2.2 on 2021-03-21 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tally', '0002_auto_20210321_1359'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trialbalance',
            name='custom_group',
        ),
        migrations.RemoveField(
            model_name='trialbalance',
            name='ledger',
        ),
        migrations.DeleteModel(
            name='Ledger',
        ),
        migrations.DeleteModel(
            name='TrialBalance',
        ),
    ]
