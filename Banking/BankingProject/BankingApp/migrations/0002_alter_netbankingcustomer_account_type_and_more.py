# Generated by Django 4.2.8 on 2024-01-16 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BankingApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='netbankingcustomer',
            name='Account_type',
            field=models.CharField(max_length=1),
        ),
        migrations.AlterField(
            model_name='netbankingcustomer',
            name='Address',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='netbankingcustomer',
            name='Gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], default='O', max_length=1),
        ),
        migrations.AlterField(
            model_name='netbankingcustomer',
            name='Materials',
            field=models.CharField(choices=[('B', 'Cheque Book'), ('D', 'Debit Card'), ('C', 'Credit Card')], default='C', max_length=1),
        ),
    ]