from django.contrib import admin
from .models import User, Profile
from django.contrib.auth.admin import UserAdmin as BaseAdmin

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class UserAdmin(BaseAdmin):
    model = User
    inlines = [ProfileInline]
    list_display = ("email", "is_staff", "is_active",)
    list_filter = ("email", "is_staff", "is_active",)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ("Permissions", {"fields": ('is_staff', 'is_active', 'groups', 'user_permissions')})
    )

    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions"
            )}
        ),
    )
    search_fields = ("email",)
    ordering = ("email",)
    
admin.site.register(User, UserAdmin)