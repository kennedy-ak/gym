from django.contrib import admin
from .models import Booking


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    """Admin interface for Booking model"""

    list_display = ['full_name', 'email', 'phone_number', 'service', 'status', 'created_at']
    list_filter = ['status', 'service', 'created_at']
    search_fields = ['full_name', 'email', 'phone_number', 'location', 'job_title']
    readonly_fields = ['created_at', 'updated_at']

    fieldsets = (
        ('Contact Information', {
            'fields': ('full_name', 'email', 'phone_number', 'job_title')
        }),
        ('Location Details', {
            'fields': ('location', 'address')
        }),
        ('Service Details', {
            'fields': ('service', 'additional_notes')
        }),
        ('Status & Management', {
            'fields': ('status', 'admin_notes', 'user')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    actions = ['mark_as_contacted', 'mark_as_completed', 'mark_as_cancelled']

    def mark_as_contacted(self, request, queryset):
        """Mark selected bookings as contacted"""
        updated = queryset.update(status='contacted')
        self.message_user(request, f'{updated} booking(s) marked as contacted.')
    mark_as_contacted.short_description = 'Mark selected as Contacted'

    def mark_as_completed(self, request, queryset):
        """Mark selected bookings as completed"""
        updated = queryset.update(status='completed')
        self.message_user(request, f'{updated} booking(s) marked as completed.')
    mark_as_completed.short_description = 'Mark selected as Completed'

    def mark_as_cancelled(self, request, queryset):
        """Mark selected bookings as cancelled"""
        updated = queryset.update(status='cancelled')
        self.message_user(request, f'{updated} booking(s) marked as cancelled.')
    mark_as_cancelled.short_description = 'Mark selected as Cancelled'
