# filepath: patients/admin.py
from django.contrib import admin
from .models import Patient
from accounts.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

class PatientInline(admin.StackedInline):  # Or use admin.TabularInline for a more compact layout
    model = Patient
    can_delete = False  # Prevent deleting the Patient object from the User admin
    verbose_name_plural = 'Patient'
    fk_name = 'user'  # Specify the foreign key field

class UserAdmin(BaseUserAdmin):
    inlines = (PatientInline,)
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'user_type')

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(UserAdmin, self).get_inline_instances(request, obj)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

# Unregister PatientAdmin
# admin.site.unregister(Patient)