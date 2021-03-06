# Generated by Django 2.2 on 2021-01-12 11:01

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SiteUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('mobile', models.CharField(max_length=10, unique=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 10 digits allowed.", regex='^\\+?1?\\d{9,10}$')])),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email-id')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('password_text', models.CharField(max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('dob', models.DateField(blank=True, null=True)),
                ('user_type', models.CharField(max_length=20, verbose_name='Type Of User')),
                ('auto_timedate', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
