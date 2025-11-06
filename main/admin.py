from django.contrib import admin
from .models import Category, DesignRequest

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(DesignRequest)
class DesignRequestAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'category', 'status', 'created_at']
    list_filter = ['status', 'category', 'created_at']
    readonly_fields = ['created_at']

    def get_readonly_fields(self, request, obj=None):
        if obj and obj.status != 'new':
            return self.readonly_fields + ('status',)
        return self.readonly_fields