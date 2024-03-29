from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

from userprofile.models import *


class CustomUserAdmin(UserAdmin):
    """Define admin model for custom User model with no username field."""
    fieldsets = (
        (None, {'fields': ('email', 'password', 'mobile', 'is_vendor')}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                       'groups', 'user_permissions')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('first_name', 'last_name', 'mobile', 'email', 'password1', 'password2', 'is_vendor'),
        }),
    )
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'mobile', 'is_vendor')
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)


admin.site.register(get_user_model(), CustomUserAdmin)

def __str__(self):
    return self.email






















