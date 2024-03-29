# Generated by Django 4.2.8 on 2024-01-16 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BankingApp', '0002_alter_netbankingcustomer_account_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='netbankingcustomer',
            name='Gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1),
        ),
        migrations.AlterField(
            model_name='netbankingcustomer',
            name='Materials',
            field=models.CharField(choices=[('B', 'Cheque Book'), ('D', 'Debit Card'), ('C', 'Credit Card')], max_length=1),
        ),
    ]
