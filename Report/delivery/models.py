from django.db import models
from  .choices import DELIVERY_STATUS
# Create your models here.
class Delivery(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    full_name = models.CharField(verbose_name='Ф.И.О',
                                max_length=250)
    status = models.CharField(max_length=250,
                            verbose_name='Статус',
                            choices=DELIVERY_STATUS)
    def __str__(self):
        return self.full_name
    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставкаы'
