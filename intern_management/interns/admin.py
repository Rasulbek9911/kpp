from django.contrib import admin
from django.utils.html import format_html
from .models import Intern


@admin.register(Intern)
class InternAdmin(admin.ModelAdmin):
    list_display = [
        'photo_preview_display',
        'full_name',
        'passport_id',
        'department',
        'reason',
        'start_date',
        'end_date',
        'days_left',
        'status_display'
    ]
    list_filter = ['department', 'created_at']
    search_fields = ['full_name', 'passport_id', 'department']
    readonly_fields = ['photo_preview_display', 'created_at', 'updated_at', 'days_left', 'status']
    
    fieldsets = (
        ('Shaxsiy ma\'lumotlar', {
            'fields': ('full_name', 'passport_id', 'photo', 'photo_preview_display')
        }),
        ('Ish ma\'lumotlari', {
            'fields': ('department', 'reason', 'start_date', 'end_date')
        }),
        ('Holati', {
            'fields': ('days_left', 'status')
        }),
        ('Vaqt ma\'lumotlari', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    def photo_preview_display(self, obj):
        """Display photo preview in admin"""
        if obj.photo:
            return format_html(
                '<img src="{}" width="50" height="50" style="border-radius: 5px;"/>',
                obj.photo.url
            )
        return '-'
    photo_preview_display.short_description = 'Rasm'

    def status_display(self, obj):
        """Display status with colors"""
        if obj.status == 'Faol':
            color = 'green'
            text = 'Faol'
        else:
            color = 'red'
            text = 'Tugagan'
        return format_html(
            '<span style="color: white; background-color: {}; padding: 5px 10px; border-radius: 3px;">{}</span>',
            color,
            text
        )
    status_display.short_description = 'Holati'

    def days_left(self, obj):
        """Display days left"""
        return obj.days_left
    days_left.short_description = 'Qolgan kunlar'

    # Make fields read-only
    def get_readonly_fields(self, request, obj=None):
        readonly = list(self.readonly_fields)
        return readonly
