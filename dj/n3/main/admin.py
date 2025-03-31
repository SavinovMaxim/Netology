from django.contrib import admin
from .models import Car, Sale, Client
from django.utils.html import format_html

class CarAdmin(admin.ModelAdmin):
    list_display = ('model', 'year', 'color', 'price', 'display_image')
    list_filter = ('year', 'body_type', 'fuel_type')
    search_fields = ('model', 'color')
    
    def display_image(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="50" height="50" />', obj.image.url)
        return "Нет изображения"
    display_image.short_description = 'Изображение'

class SaleAdmin(admin.ModelAdmin):
    list_display = ('car', 'client', 'created_at')
    list_filter = ('created_at',)
    date_hierarchy = 'created_at'

admin.site.register(Car, CarAdmin)
admin.site.register(Sale, SaleAdmin)
admin.site.register(Client)