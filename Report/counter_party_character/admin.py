from django.contrib import admin
from .models import CounterPartyCharacter
# Register your models here.

@admin.register(CounterPartyCharacter)
class CounterPartyCharacterAdmin(admin.ModelAdmin):
    pass