from django.contrib import admin

from .models import Product, Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "username", "contact"
    list_display_links = "pk", "name", "username"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = "pk", "name", "ccal"
    list_display_links = "pk", "name"