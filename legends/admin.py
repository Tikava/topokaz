from django.contrib import admin
from .models import Legend, Category


class LegendAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'author', 'date_created')
    search_fields = ('title', 'location', 'author')
    list_filter = ('location', 'author', 'date_created')
    fields = ('title', 'description', 'location', 'author', 'image')  # Add the 'image' field here

    
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Legend, LegendAdmin)
