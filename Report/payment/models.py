from django.db import models
from django.contrib.auth.models import User
from .choices import  TYPE

# Create your models here.
class Payment(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField(verbose_name='Цена')
    delivery = models.ForeignKey('delivery.Delivery',
                                on_delete=models.CASCADE,
                                verbose_name='Доставка' ,null=True, blank=True)
    counter_party = models.ForeignKey('counter_party.CounterParty',
                                        on_delete=models.CASCADE,
                                        verbose_name='Контрагент')
    pay_type = models.CharField(verbose_name='Тип журнала платежей',
                                        choices=TYPE,
                                        max_length=250)

    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name ='Журнал платежей'
        verbose_name_plural = 'Журналы платежей'