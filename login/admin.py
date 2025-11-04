# login/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, ClienteProfile, EntrenadorProfile

# ----------------------------
# Inlines para perfiles
# ----------------------------

class ClienteProfileInline(admin.StackedInline):
    model = ClienteProfile
    can_delete = False
    verbose_name_plural = 'Perfil de Cliente'

class EntrenadorProfileInline(admin.StackedInline):
    model = EntrenadorProfile
    can_delete = False
    verbose_name_plural = 'Perfil de Entrenador'

# ----------------------------
# Admin para CustomUser
# ----------------------------

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ['username', 'email', 'role', 'is_staff']
    list_filter = ['role', 'is_staff']
    fieldsets = UserAdmin.fieldsets + (
        ('Rol', {'fields': ('role',)}),
    )
    
    # Mostrar el perfil correspondiente según el rol
    def get_inline_instances(self, request, obj=None):
        inlines = []
        if obj is not None:
            if obj.role == 'cliente':
                inlines.append(ClienteProfileInline(self.model, self.admin_site))
            elif obj.role == 'trainer':
                inlines.append(EntrenadorProfileInline(self.model, self.admin_site))
        return inlines

# ----------------------------
# Admin para perfiles (opcional)
# ----------------------------

@admin.register(ClienteProfile)
class ClienteProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'fecha_nacimiento', 'telefono', 'reporte_deudas']
    search_fields = ['user__username', 'telefono']

@admin.register(EntrenadorProfile)
class EntrenadorProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'especialidad']
    search_fields = ['user__username', 'especialidad']
