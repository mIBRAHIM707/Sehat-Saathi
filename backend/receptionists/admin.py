# filepath: receptionists/admin.py
from django.contrib import admin
from .models import Receptionist
from accounts.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class ReceptionistInline(admin.StackedInline):  # Or use admin.TabularInline for a more compact layout
    model = Receptionist
    can_delete = False  # Prevent deleting the Receptionist object from the User admin
    verbose_name_plural = 'Receptionist'
    fk_name = 'user'  # Specify the foreign key field
    readonly_fields = ('employee_id',)  # Make employee_id read-only

class UserAdmin(BaseUserAdmin):
    inlines = (ReceptionistInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'user_type')

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Unregister ReceptionistAdmin
# admin.site.unregister(Receptionist)