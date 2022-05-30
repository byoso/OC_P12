# Generated by Django 4.0.4 on 2022-05-30 19:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0019_alter_employeeevent_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeclient',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignment', to='events.client'),
        ),
        migrations.AlterField(
            model_name='employeecontract',
            name='contract',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assignment', to='events.contract'),
        ),
    ]
