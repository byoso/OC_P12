# Generated by Django 4.0.4 on 2022-05-24 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0015_alter_employeeclient_client_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='assignee',
        ),
        migrations.RemoveField(
            model_name='contract',
            name='assignee',
        ),
        migrations.RemoveField(
            model_name='event',
            name='assignee',
        ),
    ]
