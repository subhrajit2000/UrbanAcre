from django.contrib import admin
from .models import Listing

@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'sale_type', 'price', 'is_published', 'list_date')
    list_filter = ('sale_type', 'house_type', 'is_published')
    search_fields = ('title', 'location', 'description')
