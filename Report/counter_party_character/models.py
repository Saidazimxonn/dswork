from django.db import models
from django.contrib.auth.models import User

# Create your models here.
                                     
class CounterPartyCharacter(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(verbose_name='Описание',
                                    null=True, blank=True)
    user = models.ForeignKey(User,
                            on_delete=models.CASCADE)
    def __str__(self):
        return str(self.user)

    class Meta:
        verbose_name = 'Характер'
        verbose_name_plural = 'Характеры'