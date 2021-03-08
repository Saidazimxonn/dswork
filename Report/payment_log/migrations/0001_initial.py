# Generated by Django 3.1.3 on 2021-03-06 10:08

import django.contrib.auth.base_user
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('delivery', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=250, verbose_name=django.contrib.auth.base_user.AbstractBaseUser.get_username)),
                ('amount', models.FloatField(verbose_name='Цена')),
                ('commit', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('outcat', models.FloatField(default=0)),
                ('outlay', models.FloatField(default=0)),
                ('payment_type', models.CharField(choices=[('S', 'Сум'), ('D', 'Доллар')], max_length=250, verbose_name='Тип оплаты')),
                ('outlay_child', models.FloatField(default=0)),
                ('payment_method', models.CharField(choices=[('enumeration', 'Перечисление'), ('cash', 'Наличное')], max_length=250, verbose_name='Метод оплаты')),
                ('payment_log_type', models.CharField(choices=[('Out', 'Превзойти'), ('In', 'Доход')], max_length=250, verbose_name='Тип журнала платежей')),
                ('delivery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='delivery.delivery', verbose_name='Доставка')),
            ],
            options={
                'verbose_name': 'Журнал платежей',
                'verbose_name_plural': 'Журналы платежей',
            },
        ),
    ]