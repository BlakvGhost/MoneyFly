# Generated by Django 4.2.4 on 2023-09-07 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banque', '0002_transactions_ref'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='balance',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
