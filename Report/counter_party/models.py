from django.db import models
from .choices import COUNTER_PARTY_STATUS


class CounterParty(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(verbose_name='Ф.И.О',
                                 max_length=250)
    balance_usd = models.FloatField(default=0,
                                    verbose_name='USD')
    balance_uzs = models.FloatField(default=0,
                                    verbose_name='UZS')
    description = models.TextField(verbose_name='Описание',
                                    null=True, blank=True)
    status = models.CharField(max_length=250,
                            verbose_name='Статус',
                            choices=COUNTER_PARTY_STATUS)
    organization = models.CharField(verbose_name='Организация',
                                    max_length=250, null=True, blank=True)
    phone = models.CharField(verbose_name='Телефон',
                            max_length=250, null=True, blank=True)
    phone_2 = models.CharField(verbose_name='Второй телефон',
                                max_length=250, null=True, blank=True)
    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name = 'Контр агент'
        verbose_name_plural = 'Контр агенты'
