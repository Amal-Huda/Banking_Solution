# Generated by Django 4.2.8 on 2024-01-16 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BankingApp', '0003_alter_netbankingcustomer_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='netbankingcustomer',
            name='Account_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='netbankingcustomer',
            name='Gender',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='netbankingcustomer',
            name='Materials',
            field=models.CharField(max_length=100),
        ),
    ]