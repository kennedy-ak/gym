from django.contrib import admin
from .models import BlogPost, HealthTip

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'is_published', 'published_at', 'created_at']
    list_filter = ['is_published', 'created_at', 'author']
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'created_at'

    def save_model(self, request, obj, form, change):
        if not change:  # If creating a new object
            obj.author = request.user
        super().save_model(request, obj, form, change)

@admin.register(HealthTip)
class HealthTipAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_active', 'created_at']
    list_filter = ['category', 'is_active', 'created_at']
    search_fields = ['title', 'content']
