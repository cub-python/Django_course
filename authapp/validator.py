from django.core.exceptions import ValidatioError
from django.utils.translation import ugettext_lazy as_

def validate_name(value):
    if value.isdigit():
        raise ValidationError(
            _(f'Имя не может быть только цифры')
            params={'value': value},
        )
    if value.isalpha():
        raise ValidationError(
            _(f'Имя не может содержать цифры')
            param={'value': value},
        )