from django.db import models


class CustomDateTimeFieldCustom(models.DateTimeField):
    """Se add for True significa que o objeto está sendo criado, nesse caso queremos que o valor do campo seja None
    """

    def pre_save(self, model_instance, add):
        if add:
            return None
        return super().pre_save(model_instance, add)


class CreatedUpdatedAtMixin(models.Model):
    created_at = models.DateTimeField('criado em', auto_now_add=True)
    updated_at = CustomDateTimeFieldCustom('atualizado em', auto_now=True, blank=True, null=True)

    class Meta:
        abstract = True
