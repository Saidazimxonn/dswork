from django.db import models
from django.contrib.auth.models import User
from .choices import PAYMENT_TYPE, PAYMENT_METHOD, PAYMENT_LOG_TYPE

# Create your models here.
class PaymentLog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.FloatField(verbose_name='Цена')
    commit = models.TextField(verbose_name='Комментарий',
                                null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    outcat = models.FloatField(default=0)
    outlay = models.FloatField(default=0)
    payment_type = models.CharField(verbose_name='Тип оплаты',
                                    choices=PAYMENT_TYPE,
                                    max_length=250)
    outlay_child = models.FloatField(default=0)
    payment_method = models.CharField(verbose_name='Метод оплаты',
                                      choices=PAYMENT_METHOD,
                                      max_length=250)

    payment_log_type = models.CharField(verbose_name='Тип журнала платежей',
                                        choices=PAYMENT_LOG_TYPE,
                                        max_length=250)
    delivery = models.ForeignKey('delivery.Delivery',
                                on_delete=models.CASCADE,
                                verbose_name='Доставка')
    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name ='Журнал платежей'
        verbose_name_plural = 'Журналы платежей'