from django.contrib import admin
from .models import Product, SalesCheck


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    ordering = ('name', 'value')
    search_fields = ('name', 'description')


class SalesCheckAdmin(admin.ModelAdmin):
    list_display = ('date', 'totalToPay')
    ordering = ('date',)
    search_fields = ('date', 'totalToPay')


admin.site.register(Product, ProductAdmin)
admin.site.register(SalesCheck, SalesCheckAdmin)
