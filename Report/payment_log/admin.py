from django.contrib import admin
from .models import PaymentLog
# Register your models here.
@admin.register(PaymentLog)
class PaymentLogAdmin(admin.ModelAdmin):
    pass