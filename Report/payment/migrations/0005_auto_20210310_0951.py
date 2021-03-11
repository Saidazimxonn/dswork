# Generated by Django 3.1.3 on 2021-03-10 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_auto_20210310_0918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='pay_type',
            field=models.CharField(choices=[('Income', 'Доход'), ('Outcome', 'Расходы')], max_length=250, verbose_name='Тип журнала платежей'),
        ),
    ]