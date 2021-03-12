from django.contrib import admin
from .models import Delivery
# Register your models here.
@admin.register(Delivery)
class DeliveryAdmin(admin.ModelAdmin):
   list_display = ('full_name', 'status')
   list_display_links =  ('full_name', 'status')
   list_filter = ('created', 'status')
