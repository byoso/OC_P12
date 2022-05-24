# Generated by Django 4.0.4 on 2022-05-24 02:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0013_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeclient',
            name='client',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.client'),
        ),
        migrations.AlterField(
            model_name='employeecontract',
            name='client',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.contract'),
        ),
        migrations.AlterField(
            model_name='employeeevent',
            name='client',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='events.event'),
        ),
    ]