from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from users.models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (
            ('Personal info'),
            {'fields': ('username', 'first_name', 'last_name', 'phone_number')}
        ),
        (('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser',
                                      'groups', 'user_permissions')}),
        (('Important dates'), {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    list_display = (
        'username',
        'id',
        'email',
        'first_name',
        'last_name',
    )
    list_filter = ('email',)
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email',)
