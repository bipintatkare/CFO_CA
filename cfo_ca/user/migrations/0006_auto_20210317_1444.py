# Generated by Django 2.2 on 2021-03-17 09:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20210311_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='siteuser',
            name='user_type',
            field=models.CharField(choices=[('employee', 'Employee user'), ('partner', 'Partner user'), ('admoin', 'Admin user')], default='employee', max_length=20),
        ),
    ]