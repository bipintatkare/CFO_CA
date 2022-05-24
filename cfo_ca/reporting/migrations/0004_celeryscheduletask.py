# Generated by Django 2.2 on 2021-03-16 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_celery_beat', '0014_remove_clockedschedule_enabled'),
        ('reporting', '0003_auto_20210315_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='CeleryScheduleTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=70)),
                ('task_name', models.CharField(blank=True, choices=[('mis_schedule_mail_task', 'mis_schedule_mail_task'), ('task_meeting_thread', 'task_meeting_thread'), ('notify_meeting_create', 'notify_meeting_create'), ('notify_meeting_close', 'notify_meeting_close'), ('meeting_reminder', 'meeting_reminder'), ('mis_schedule_mail_task', 'mis_schedule_mail_task'), ('meeting_reminder', 'meeting_reminder'), ('task_reminder', 'task_reminder')], max_length=40, null=True)),
                ('cron', models.CharField(blank=True, max_length=70)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('task', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='celery_schedular', to='django_celery_beat.PeriodicTask')),
            ],
        ),
    ]