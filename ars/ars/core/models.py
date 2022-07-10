from ars.core.mixins import CreatedUpdatedAtMixin
from django.conf import settings
from django.contrib.postgres.fields import CIEmailField
from django.db import models
from django.utils.translation import gettext_lazy as _


class Profile(CreatedUpdatedAtMixin):
    MANAGER = 'MANAGER'
    ANALYST = 'ANALYST'
    ASSISTANT = 'ASSISTANT'

    OCCUPATION = (
        (MANAGER, 'Gerente'),
        (ANALYST, 'Analista'),
        (ASSISTANT, 'Assistente'),
    )

    ADMINISTRATOR = 'ADMINISTRATOR'
    CONTROLLER = 'CONTROLLER'
    VISITOR = 'VISITOR'
    PROVIDER = 'PROVIDER'
    EMPLOYEE = 'EMPLOYEE'

    PROFILE_NAME = (
        (ADMINISTRATOR, 'Administrador'),
        (CONTROLLER, 'Auditor'),
        (VISITOR, 'Visitante'),
        (PROVIDER, 'Fornecedor'),
        (EMPLOYEE, 'Funcionário'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True,
                             verbose_name='usuário Django')
    name = models.CharField(_("name"), max_length=150, blank=True)
    email = CIEmailField(
        _("email address"),
        unique=True,
        error_messages={
            "unique": _("A user with that email address already exists."),
        },
    )
    perfil_name = models.CharField('função', max_length=20, choices=PROFILE_NAME)
    ocuppation = models.CharField('ocupação', max_length=20, choices=OCCUPATION, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Perfil'
        verbose_name_plural = 'Perfis'
