# Generated by Django 4.0.4 on 2022-05-24 03:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0016_remove_client_assignee_remove_contract_assignee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employeeclient',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='employeeclient',
            name='date_revoked',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employeecontract',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='employeecontract',
            name='date_revoked',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='employeeevent',
            name='date_created',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='employeeevent',
            name='date_revoked',
            field=models.DateField(blank=True, null=True),
        ),
    ]
