from django.contrib import admin

from .models import Category, Joke

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category 
    list_display = ['category', 'created', 'updated']

    def get_readonly_fields(self, request, obj=None):
        if obj: # editing an existing object
            return ('slug', 'created', 'updated')

        return ()

