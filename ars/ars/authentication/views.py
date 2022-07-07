from django.contrib.auth.views import PasswordResetConfirmView
from django.views.generic import UpdateView

from .forms import CustomSetPasswordForm
from .models import CustomUser


class CustomPasswordResetConfirmView(PasswordResetConfirmView):
    form_class = CustomSetPasswordForm


class EditAccountView(UpdateView):
    fields = ('name', 'email', 'password')
    model = CustomUser
