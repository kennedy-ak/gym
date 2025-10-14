from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    list_display = ['username', 'email', 'phone_number', 'is_approved', 'is_staff', 'date_joined']
    list_filter = ['is_approved', 'is_staff', 'is_active', 'date_joined']
    search_fields = ['username', 'email', 'phone_number']

    fieldsets = UserAdmin.fieldsets + (
        ('Additional Info', {'fields': ('phone_number', 'date_of_birth', 'address', 'profile_picture')}),
        ('Approval', {'fields': ('is_approved',)}),
    )

    actions = ['approve_users', 'unapprove_users']

    def approve_users(self, request, queryset):
        queryset.update(is_approved=True)
        self.message_user(request, f'{queryset.count()} users have been approved.')
    approve_users.short_description = "Approve selected users"

    def unapprove_users(self, request, queryset):
        queryset.update(is_approved=False)
        self.message_user(request, f'{queryset.count()} users have been unapproved.')
    unapprove_users.short_description = "Unapprove selected users"
