"""
Admin customisation.
"""

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core import models
from django.utils.translation import gettext_lazy as translate   # useful when we want to change language of the text in future. (using some configurations)

# Register your models here.

# Since we are using custom User, not default Django provided user, we will have to have custom settings also.
# Because as you see, we have used ordering here with id, by default UserAdmin uses ordering by username, and this field is not there with our custom User class.
class UserAdmin(BaseUserAdmin):
    """Define the admin pages for users."""
    ordering = ['id']
    list_display = ['email', 'name']
    
    # this configuration would be applied to admin/core/user/{id}/change admin interface.
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            translate('Permissions'),
            {
                'fields':(
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (translate('Important dates'), {'fields': ('last_login',)}),
    )
    readonly_fields = ['last_login']
    
    # add_fieldsets will modify the add user page in admin interface
    # we can have lists also, at the place of tuple (has to be an iterable object, see documentation)
    add_fieldsets = (
        (None, {
            'classes': ('wide',),     #  it is CSS, this makes the page a little wider
            'fields': (
                'email',
                'password1',
                'password2',
                'name',
                'is_active',
                'is_staff',
                'is_superuser',
            )
        }),
    )
    
admin.site.register(models.User, UserAdmin)      # UserAdmin is provided to make sure it uses our defined custom UserAdmin class (optional)