from django.contrib import admin
from django.utils.crypto import get_random_string

from .models import Profile
from ..authentication.models import CustomUser


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'created_at', 'updated_at')
    exclude = ('user',)

    def save_form(self, request, form, change):
        form = super().save_form(request, form, change)
        form.user = create_user(form.name, form.email, is_staff=False)
        return form


def create_user(name, email, is_staff=False) -> CustomUser:
    password = get_random_string(12)
    user: CustomUser = CustomUser.objects.create_user(email, password, name=name, is_staff=is_staff)

    user.email_user(
        'Dados de acesso', f'Login: {email}\nSenha: {password}',
    )
    return user
