# Generated by Django 2.2 on 2021-03-24 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tally', '0004_ledger_trialbalance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trialbalance',
            name='ledger',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='import_app.Ledgers'),
        ),
    ]
