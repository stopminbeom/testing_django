from django.contrib import admin
from .models import Product, OpenApi

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )

@admin.register(OpenApi)
class OpenApi(admin.ModelAdmin):
    list_display = (
        'id',
        'item_name',
        'kind_name',
        'rank',
        'unit',
    )
