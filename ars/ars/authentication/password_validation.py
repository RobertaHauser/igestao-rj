from django.contrib.auth.password_validation import CommonPasswordValidator, NumericPasswordValidator, \
    UserAttributeSimilarityValidator


class CustomUserAttributeSimilarityValidator(UserAttributeSimilarityValidator):
    def get_help_text(self):
        return 'Sua senha não pode ser muito parecida com suas outras informações pessoais.'


class CustomCommonPasswordValidator(CommonPasswordValidator):
    def get_help_text(self):
        return 'Sua senha não pode ser uma senha comumente usada.'


class CustomNumericPasswordValidator(NumericPasswordValidator):
    def get_help_text(self):
        return 'Sua senha não pode ser totalmente numérica.'
