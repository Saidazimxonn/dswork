from django.contrib import admin
from .models import CounterParty  
# Register your models here.
@admin.register(CounterParty)
class CounterPartyAdmin(admin.ModelAdmin):
    pass