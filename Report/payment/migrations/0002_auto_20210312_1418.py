# Generated by Django 3.1.3 on 2021-03-12 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='pay_type',
            field=models.CharField(choices=[('Outcome', 'Расходы'), ('Income', 'Доход')], max_length=250, verbose_name='Тип журнала платежей'),
        ),
    ]
