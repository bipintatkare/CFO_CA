# Generated by Django 2.2 on 2021-04-10 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reporting', '0016_auto_20210407_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScriptMaster',
            fields=[
                ('script_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('execution_time', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ScriptMaster',
                'verbose_name_plural': 'ScriptMaster',
                'ordering': ['-created_at'],
            },
        ),
    ]
