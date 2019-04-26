from django.contrib import admin
from .models import Product, SalesCheck, Line


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')
    ordering = ('name', 'value')
    search_fields = ('name', 'description')


class LineInLine(admin.TabularInline):
    model = Line
    readonly_fields = ('product', 'value', 'cuantity', 'totalValue')


class SalesCheckAdmin(admin.ModelAdmin):
    inlines = [
        LineInLine,
    ]
    list_display = ('date', 'totalToPay')
    ordering = ('date',)
    search_fields = ('date', 'totalToPay')


admin.site.register(Product, ProductAdmin)
admin.site.register(SalesCheck, SalesCheckAdmin)
