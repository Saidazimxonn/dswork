from django.contrib import admin
from .models import Payment
# Register your models here.
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'counter_party', 'pay_type')
    list_display_links = ('user', 'amount', 'counter_party', 'pay_type')
    list_filter = ('user', 'counter_party', 'pay_type')