from django.contrib.auth.forms import SetPasswordForm


class CustomSetPasswordForm(SetPasswordForm):
    error_messages = {
        'password_mismatch': 'Os dois campos de senha não correspondem.',
    }
