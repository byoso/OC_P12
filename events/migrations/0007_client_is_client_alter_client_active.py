# Generated by Django 4.0.4 on 2022-05-18 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_alter_client_active_alter_event_contract'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='is_client',
            field=models.BooleanField(default=False, verbose_name='is client'),
        ),
        migrations.AlterField(
            model_name='client',
            name='active',
            field=models.BooleanField(default=False),
        ),
    ]
