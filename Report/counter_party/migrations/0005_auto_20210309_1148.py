# Generated by Django 3.1.3 on 2021-03-09 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter_party', '0004_auto_20210309_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counterparty',
            name='status',
            field=models.CharField(choices=[('not active', 'не активен'), ('active', 'активен')], max_length=250, verbose_name='Статус'),
        ),
    ]
