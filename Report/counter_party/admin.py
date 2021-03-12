from django.contrib import admin
from .models import CounterParty  
# Register your models here.
@admin.register(CounterParty)
class CounterPartyAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'status', 'organization')
    list_display_links = ('full_name', 'status', 'organization')
    list_filter = ('created','full_name','status', )