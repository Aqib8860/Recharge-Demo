from django.contrib import admin
from .models import Recharge

# Register your models here.


@admin.register(Recharge)
class RechargeAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'plan', 'recharge_date']
